from flask import request, jsonify
from app import app, db
from models import Goal, Score
import random

@app.route('/api/goals', methods=['POST'])
def add_goal():
    data = request.json
    new_goal = Goal(goal=data['goal'])
    db.session.add(new_goal)
    db.session.commit()
    return jsonify({'message': 'Goal added successfully'}), 201

@app.route('/api/scores', methods=['POST'])
def add_score():
    data = request.json
    new_score = Score(score=data['score'])
    db.session.add(new_score)
    db.session.commit()
    return jsonify({'message': 'Score added successfully'}), 201

@app.route('/api/ranking', methods=['GET'])
def get_ranking():
    scores = Score.query.order_by(Score.score.desc()).all()
    ranking = [{'rank': i+1, 'score': score.score} for i, score in enumerate(scores)]

    # ランダムにダミーを追加
    for _ in range(5):  # 例えば5つのダミーを追加
        dummy_rank = random.randint(1, len(ranking) + 1)
        ranking.insert(dummy_rank - 1, {'rank': dummy_rank, 'score': random.randint(0, 100)})

    # 順位を再計算
    for i, item in enumerate(ranking):
        item['rank'] = i + 1
    
    # ユーザーのスコア上昇値による順位調整（例としてランダムに上昇値を加える）
    user_score_increase = random.randint(1, 10)  # 仮の上昇値
    user_score = 50  # 仮のユーザースコア
    for item in ranking:
        if item['score'] == user_score:
            item['score'] += user_score_increase

    ranking.sort(key=lambda x: x['score'], reverse=True)
    
    # 再度順位を再計算
    for i, item in enumerate(ranking):
        item['rank'] = i + 1

    return jsonify(ranking)

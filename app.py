from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# モデルのインポートは db の初期化後に行う
from models import Goal, Score
import routes

if __name__ == '__main__':
    app.run(debug=True)

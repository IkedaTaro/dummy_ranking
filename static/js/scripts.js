document.getElementById('goalForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const goal = document.getElementById('goalInput').value;
    fetch('/api/goals', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ goal: goal })
    }).then(response => response.json()).then(data => {
        console.log(data);
    });
});

document.getElementById('scoreForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const score = document.getElementById('scoreInput').value;
    fetch('/api/scores', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ score: score })
    }).then(response => response.json()).then(data => {
        console.log(data);
    });
});

function loadRanking() {
    fetch('/api/ranking')
        .then(response => response.json())
        .then(data => {
            const rankingDiv = document.getElementById('ranking');
            rankingDiv.innerHTML = '';
            data.forEach(item => {
                const div = document.createElement('div');
                div.textContent = `順位: ${item.rank}, スコア: ${item.score}`;
                rankingDiv.appendChild(div);
            });
        });
}

loadRanking();

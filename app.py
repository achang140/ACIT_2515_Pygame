from flask import Flask, render_template, request 
from models.logic import Logic

app = Flask(__name__)

@app.route("/")
def home():
    data = Logic("data.json") 
    best_player = data.best
    names = data.players
    scores = data.best_score
    time = data.best_time
    length = len(names)

    return render_template("home.html", result=best_player, names=names, scores=scores, time=time, length=length)

@app.route("/player")
def one_player():
    data = Logic("data.json")
    name = request.args.get("username")
    scores, time = data.one_player_data(name)
    length = len(scores)
    return render_template("player.html", playername=name, scores=scores, time=time, length=length)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
from flask import Flask, render_template, request 
from models import Logic

app = Flask(__name__)

@app.route("/")
def home():
    data = Logic("data.json") 
    best_player = data.best
    names = data.players
    scores = data.best_score
    time = data.best_time
    played_times = data.played_times
    length = len(names)

    return render_template("home.html", result=best_player, names=names, scores=scores, time=time, played_times=played_times, length=length)

@app.route("/player")
def one_player():
    data = Logic("data.json")
    name = request.args.get("username")
    scores, time, top_score, top_time, times_played = data.one_player_data(name)
    length = len(scores)
    return render_template("player.html", playername=name, scores=scores, time=time, top_score=top_score, top_time=top_time, times_played=times_played, length=length)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
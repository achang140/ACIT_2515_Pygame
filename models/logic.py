import json 

class Logic:
    def __init__(self, filename):
        self.filename = filename 
        
        self.all_data = []

        # Name of Players 
        self.players = [] 
        # History of Players 
        self.players_info = []
        
        # All Scores of Each Player  
        self.scores = []
        # All Times 
        self.time = []

        self.best_score = []
        self.best_time = []

        # Top Player with Best Score 
        self.best = {} # Dictionary contains best user's name, score, and time 

        self.load_from_json()
        self.best_player()

    def load_from_json(self):
        with open("data.json", "r") as fp: 
            data = json.load(fp)

            for i in data: 
                self.all_data.append(i)

            for data_name, data_history in data.items():
                self.players.append(data_name)
                self.players_info.append(data_history)

            for info in self.players_info:
                self.scores.append(info["Score"]) # All Scores 
                self.time.append(info["Time"]) # All Times 

                highest_score = max(info["Score"])
                index_of_score = info["Score"].index(highest_score)
                time_of_score = info["Time"][index_of_score]
                self.best_score.append(highest_score) # Highest Score 
                self.best_time.append(time_of_score) # Time of the Highest Score 

    def best_player(self):
        best_score = max(self.best_score)
        index_of_best_score = self.best_score.index(best_score)
        self.best["best_player"] = self.players[index_of_best_score]
        self.best["best_score"] = best_score
        self.best["time"] = self.best_time[index_of_best_score]

    def one_player_data(self, playername):
        index = self.players.index(playername)
        self.one_player_score = self.scores[index]
        self.one_player_time = self.time[index]
        return self.one_player_score, self.one_player_time

    # def one_player_best_data(self, )
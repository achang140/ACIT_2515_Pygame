import json 

class Logic:
    """ 
    Logic Class for Flask 
    """
    def __init__(self, filename):
        """ Constructs necessary components for Logic Class """
        # JSON File 
        self.filename = filename 
        # Whole JSON File into a Dictionary 
        self.all_data = {}
        self.new_sorted = {}
        
        # Name of All Players 
        self.players = [] 
        # History of All Players (Scores and Times)
        self.players_info = []
        
        # All Scores of Each Player  
        self.scores = []
        # All Times associated with the Scores 
        self.time = []
        # Number of Times Each Player Played 
        self.played_times = [] 

        # The Best Score of Each Player 
        self.best_score = []
        # Time associated with the Best Score 
        self.best_time = []

        # Top Player with Best Score 
        self.best = {} # Dictionary contains best user's name, score, and time 

        self.load_from_json()
        self.high_score_time()
        self.best_player()
        self.times_played()

    def load_from_json(self):
        """ 
        Open and read data.json file
        * Save the entire data.json file to the "self.all_data" list then sort by key to 
        * Save all players' names into the "self.players" list
        * Save all players' scores and times to the "self.players_info" list 
        * Save all players' scores into the list "self.scores"
        * Save all players' times assoicated with the scores into the list "self.time" 
        * Save each player's highest score and its associated time into the list "self.best_score" and "self.best_time" 
        """
        with open("data.json", "r") as fp: 
            data = json.load(fp)

            for i in data: 
                self.all_data[i] = data[i]

            for data_name, data_history in data.items():
                self.players.append(data_name)
                self.players_info.append(data_history)

    def high_score_time(self):
        """ Each player's highest score and its corresponding time """
        for info in self.players_info:
            self.scores.append(info["Score"]) # All Scores 
            self.time.append(info["Time"]) # All Times 

            highest_score = max(info["Score"]) # Highest Score 
            index_of_score = info["Score"].index(highest_score) # Index of the Highest Score 
            time_of_score = info["Time"][index_of_score] # Time of the Highest Score will be the same index as Highest Score 
            self.best_score.append(highest_score) # Highest Score of Each Player 
            self.best_time.append(time_of_score) # Time of the Highest Score 
    
    def times_played(self):
        """ Number of times each player has played the game """
        for i in self.scores: 
            self.played_times.append(len(i))

    def best_player(self):
        """ 
        Find the highest score among all players
        Append player's name, score, and the associated time to a dictionary "self.best" 
        """
        best_score = max(self.best_score) # Highest Score of All Players 
        index_of_best_score = self.best_score.index(best_score)
        self.best["best_player"] = self.players[index_of_best_score]
        self.best["best_score"] = best_score
        self.best["time"] = self.best_time[index_of_best_score]

    def one_player_data(self, playername):
        """ 
        Returns all scores and times of a specific player. 
        Return the best score and its corresponding time of a specific player. 
        Return the number of times a specific player has played the game. 
        """
        index = self.players.index(playername)
        
        self.one_player_score = self.scores[index]
        self.one_player_time = self.time[index]
        
        self.one_player_top_score = max(self.scores[index])
        self.one_player_top_time = max(self.time[index])

        self.one_player_played_times = len(self.scores[index])
        
        return self.one_player_score, self.one_player_time, self.one_player_top_score, self.one_player_top_time, self.one_player_played_times

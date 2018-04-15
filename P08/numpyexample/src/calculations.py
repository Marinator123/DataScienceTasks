import numpy as np

class Calculations:
    def __init__(self, team_statistics):
        self.team_statistics = team_statistics
        self.shots_on_goal_per_player = np.array([])
        self.goals_per_player = np.array([])    

    def get_shots_on_goal_per_player(self):
        for player in self.team_statistics:
            self.shots_on_goal_per_player = np.append(self.shots_on_goal_per_player, player['Shots on Goal'])
        return self.shots_on_goal_per_player
    
    def get_average_shots_on_goal_per_player(self):
        return np.mean(self.shots_on_goal_per_player)

    def get_std_shots_on_goal_per_player(self):
        return np.std(self.shots_on_goal_per_player)

    def get_goals_per_player(self):
        for player in self.team_statistics:
            self.goals_per_player = np.append(self.goals_per_player, player['Goals'])
        return self.goals_per_player

    def get_average_goals_per_player(self):
        return np.mean(self.goals_per_player)
    
    def get_std_goals_per_player(self):
        return np.std(self.goals_per_player)

    def get_score_per_position(self, score):
        dict_goals_per_position = {}
        for player in self.team_statistics:
            player_position = player['Position']
            goals = player[score]
            if (player_position in dict_goals_per_position):
                dict_goals_per_position[player_position] += goals
            else:
                dict_goals_per_position[player_position] = goals
        return dict_goals_per_position

    def get_linear_regression(self, xi,y):
        A = np.array([ xi, np.ones(len(xi))])
        a, b = np.linalg.lstsq(A.T,y)[0] # obtaining the parameters
        return a, b # return as a tuple
        
    def get_correlation(self, x,y):
        return x.dot(y) / (np.sqrt(x.dot(x) * y.dot(y)))

    def get_sum(self, list):
        return np.sum(list)

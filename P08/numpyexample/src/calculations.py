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

    def get_goals_by_position(self):
        dict_goals_by_position = {}
        for player in self.team_statistics:
            player_position = player['Position']
            goals = player['Goals']
            if (player_position in dict_goals_by_position):
                dict_goals_by_position[player_position] += goals
            else:
                dict_goals_by_position[player_position] = goals
        return dict_goals_by_position
                    


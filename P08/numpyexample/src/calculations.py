import numpy as np

class Calculations:
    def __init__(self, team_statistics):
        self.team_statistics = team_statistics
        self.shots_on_goal_per_player = np.array([])
        self.goals_per_player = np.array([])    

    def calculateShotsOnGoalPerPlayer(self):
        for team in self.team_statistics.values():
            for player in team:
                self.shots_on_goal_per_player = np.append(self.shots_on_goal_per_player, player['Shots on Goal'])
        return self.shots_on_goal_per_player

    def calculateGoalsPerPlayer(self):
        for team in self.team_statistics.values():
            for player in team:
                self.goals_per_player = np.append(self.goals_per_player, player['Goals'])
        return self.goals_per_player
    

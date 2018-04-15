from numpyexample.src.readexcel import read_excel
from numpyexample.src.calculations import Calculations
from numpyexample.src.plotfigures import Plots
import matplotlib.pyplot as plt

# brauche array mit allen shots on goals / goals und muss diesen dann visualisieren
def runner():
    team_statistics = read_excel('p08_hockey_stats.xlsx')

    for team, statistics in team_statistics.items():
        calc = Calculations(statistics)
        shots_on_goal = calc.get_shots_on_goal_per_player()
        average_shots_on_goal = calc.get_average_shots_on_goal_per_player()
        std_shots_on_goal = calc.get_std_shots_on_goal_per_player()
        
        goals = calc.get_goals_per_player()
        average_goals = calc.get_average_goals_per_player()
        std_goals = calc.get_std_goals_per_player()

        # Plots
        plots = Plots(team)
        plots.show_average_shots_on_goal(shots_on_goal, average_shots_on_goal, std_shots_on_goal)
        plots.show_average_goals(goals, average_goals, std_goals)
        
        goals_by_position = calc.get_goals_by_position()
        plots.show_goals_by_position(goals_by_position)

    plt.show()
    

if __name__ == '__main__':
    runner()


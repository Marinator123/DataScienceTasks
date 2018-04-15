from numpyexample.src.readexcel import read_excel
from numpyexample.src.calculations import Calculations
from numpyexample.src.plotfigures import Plots, show
import matplotlib.pyplot as plt

# brauche array mit allen shots on goals / goals und muss diesen dann visualisieren
def runner():
    team_statistics = read_excel('p08_hockey_stats.xlsx')

    for team_name, statistics in team_statistics.items():

        # Calculations
        calc = Calculations(statistics)
        shots_on_goal = calc.get_shots_on_goal_per_player()
        average_shots_on_goal = calc.get_average_shots_on_goal_per_player()
        std_shots_on_goal = calc.get_std_shots_on_goal_per_player()
        shots_on_goal_per_position = calc.get_score_per_position('Shots on Goal')
        shots_on_goal_sum = calc.get_sum(shots_on_goal)

        goals = calc.get_goals_per_player()
        average_goals = calc.get_average_goals_per_player()
        std_goals = calc.get_std_goals_per_player()
        goals_per_position = calc.get_score_per_position('Goals')
        goals_sum = calc.get_sum(goals)

        corr_goals_vs_shots = calc.get_correlation(shots_on_goal, goals)
        # Parameters of linear regression
        w = calc.get_linear_regression(shots_on_goal, goals)
        line = w[0]*shots_on_goal + w[1]

        # Plots
        plots = Plots(team_name)
        plots.show_average_shots_on_goal(shots_on_goal, average_shots_on_goal, std_shots_on_goal)
        plots.show_average_goals(goals, average_goals, std_goals)
        plots.show_goals_by_position(goals_per_position)
        plots.show_goals_vs_shots(goals, shots_on_goal, line)

        # Text Output
        print('------------------------')
        print('Summary',team_name,'with', len(goals), 'players')
        print('------------------------')    
        print('\ttotal\tmean\tby forwards\tby defense')
        print('shots\t',shots_on_goal_sum,'\t',round(average_shots_on_goal,1),'\t',shots_on_goal_per_position['Forward'],'\t',shots_on_goal_per_position['Defense']) 
        print('goals\t',goals_sum,'\t',round(average_goals,1),'\t',goals_per_position['Forward'],'\t',goals_per_position['Defense'])
        print('------------------------')
        print('success\t', round(100*goals_sum / shots_on_goal_sum,1),'%')
        print('correlation\t',round(corr_goals_vs_shots,2))
        print('regression\t','goals = ',round(w[0],2),'* shots + ',round(w[1],1))
        print()

    show()
    

if __name__ == '__main__':
    runner()


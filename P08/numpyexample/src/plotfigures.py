import matplotlib.pyplot as plt
import seaborn as sns

class Plots:
    def __init__(self, team_name):
        self.fig = plt.figure(figsize=(20,4))
        self.fig.suptitle('Stats: %s' % (team_name), fontsize=14, fontweight='bold')
        sns.set_style("darkgrid")

    def show_average_shots_on_goal(self, shots_on_goal, average, std):
        ax = self.fig.add_subplot(1,4,1)
        plt.hist(shots_on_goal)
        plt.ylabel('Number of Players')
        plt.xlabel('Shots on Goal')
        plt.yticks(list(range(0,22,2)))
        plt.title('Shots on Goal per Player')
        plt.plot(average,0.5,'o',[average-std,average+std],[0.5,0.5],'-')

    def show_average_goals(self, goals, average, std):
        ax = self.fig.add_subplot(1,4,2)
        plt.hist(goals)
        plt.ylabel('Number of Players')
        plt.xlabel('Goals')
        plt.title('Goals per Player')
        plt.plot(average,0.5,'o',[average-std,average+std],[0.5,0.5],'-')

    def show_goals_by_position(self, goals_by_position):
        ax = self.fig.add_subplot(1,4,3)
        plt.pie([goals_by_position['Forward'],goals_by_position['Defense']],
                labels=["Forward","Defense"],
                autopct='%1.1f%%', #display percentages
                colors=plt.rcParams['axes.prop_cycle'].by_key()['color']) # pie charts due not get default colors
        plt.title('Who scored?')

    def show_goals_vs_shots(self, goals, shots, line):
        ax = self.fig.add_subplot(1,4,4)
        plt.plot(shots,goals,'o',shots,line)
        plt.title('Shots vs goals')
        plt.xlabel('number of shots')
        plt.ylabel('number of goals')

def show():
    plt.show()
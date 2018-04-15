import matplotlib.pyplot as plt
import seaborn as sns

def show_average_shots_on_goal(shots_on_goal, average, std):
    plt.figure(1)
    sns.set_style("darkgrid")
    plt.hist(shots_on_goal)
    plt.ylabel('Number of Players')
    plt.xlabel('Shots on Goal')
    plt.yticks(list(range(0,22,2)))
    plt.title('Shots on Goal per Player')
    plt.plot(average,0.5,'o',[average-std,average+std],[0.5,0.5],'-')

def show_average_goals(goals, average, std):
    plt.figure(2)
    sns.set_style("darkgrid")
    plt.hist(goals)
    plt.ylabel('Number of Players')
    plt.xlabel('Goals')
    plt.title('Goals per Player')
    plt.plot(average,0.5,'o',[average-std,average+std],[0.5,0.5],'-')
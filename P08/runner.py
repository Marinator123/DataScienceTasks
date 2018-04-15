from numpyexample.src.readexcel import read_excel
from numpyexample.src.calculations import Calculations

# brauche array mit allen shots on goals / goals und muss diesen dann visualisieren
def runner():
    team_statistics = read_excel('p08_hockey_stats.xlsx')
    calc = Calculations(team_statistics)
    print(calc.calculateShotsOnGoalPerPlayer())
    print(calc.calculateGoalsPerPlayer())

if __name__ == '__main__':
    runner()


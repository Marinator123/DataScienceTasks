import numpy as np 


class Queries:
    def __init__(self, data):
        self.data = data

    """Calculates the proportion of male and female survivors of the total survivors
    """
    def proportion_gender_survival(self):
        women_onboard = [d for d in self.data if d['sex'] == 'female']
        men_onboard = [d for d in self.data if d['sex'] == 'male']

        num_women_survived = np.size(list(filter(lambda x: int(x['survived']), women_onboard)))
        num_men_survived = np.size(list(filter(lambda x: int(x['survived']), men_onboard)))

        prop_women_survived = num_women_survived / len(women_onboard)
        prop_men_survived = num_men_survived / len(men_onboard)

        return {'women_prop_survived':prop_women_survived, 'men_prop_survived': prop_men_survived}
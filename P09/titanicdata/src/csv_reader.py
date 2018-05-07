import csv
import numpy as np

def get_csv_data(filename):
    dict_list = []
    with open(filename, 'r') as f:
        csv_file = csv.reader(f, delimiter=';')
        keys = next(csv_file)
        for row in csv_file:
            d = {keys[i]: row[i] for i in range(0, len(keys))}
            dict_list.append(d)
    return np.array(dict_list)

# Testrunner
if __name__ == '__main__':
    get_csv_data('titanic3_train.csv')
from titanicdata.src import Queries, get_csv_data, write_csv_data, HandleMissingData
import numpy as np

def getKey(entry):
    return str(entry['zSex']) + str(entry['zPclass']) + str(entry['zFare_per_pclass'])

if __name__ == '__main__':
    train_data = get_csv_data('titanic3_train.csv')
    test_data = get_csv_data('titanic3_test.csv')
    
    missing_data_calc = HandleMissingData(train_data, test_data)
    
    train_data = missing_data_calc.get_fixed_train_data()
    test_data = missing_data_calc.get_fixed_test_data()

    queries = Queries(train_data)

    gender_types = queries.get_column_values(train_data, 'sex')
    pclass_types = queries.get_column_values(train_data, 'pclass')

    train_data = queries.add_attribute(train_data, 'sex', 'zSex', gender_types)
    train_data = queries.add_attribute(train_data, 'pclass', 'zPclass', pclass_types)

    pclasses_dict = queries.group_by_attribute(train_data, 'pclass')
    fare_breaks_pclass = {i: queries.get_groups_of_attribute(y, 'fare', 4) for i, y in pclasses_dict.items()}
    
    train_data = queries.add_group_attribute(train_data, 'pclass', 'fare', 'zFare_per_pclass', fare_breaks_pclass)

    survival_table = np.zeros((len(gender_types),len(pclass_types), 
        len(fare_breaks_pclass['1'])))
    
    grouped_values = {}
    for entry in train_data:
        key = getKey(entry)
        if key not in grouped_values:
            grouped_values[key] = np.array(entry)
        else:
            grouped_values[key] = np.append(grouped_values[key], entry)
    
    for j in grouped_values.values():
        index = j[0]['zSex'], j[0]['zPclass'], j[0]['zFare_per_pclass']
        survival_table[index] = queries.proportion_of_survival(j)

    test_data = queries.add_attribute(test_data, 'sex', 'zSex', gender_types)
    test_data = queries.add_attribute(test_data, 'pclass', 'zPclass', pclass_types)
    test_data = queries.add_group_attribute(test_data, 'pclass', 'fare', 'zFare_per_pclass', fare_breaks_pclass)
    
    output_data = []
    for j in test_data:
        index = j['zSex'], j['zPclass'], j['zFare_per_pclass']
        if survival_table[index] >= 0.5:
            output_data.append([j['id'], 1])
        else: 
            output_data.append([j['id'], 0])

    write_csv_data('test_submission.csv', output_data) 

# address https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/titanic.html


    
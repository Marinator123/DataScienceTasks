from titanicdata.src import Queries, get_csv_data, write_csv_data, HandleMissingData
import numpy as np
import urllib, urllib.request

def get_key(entry):
    return str(entry['zSex']) + str(entry['zPclass']) + str(entry['zFare_per_pclass']) + str(entry['zAge'])

if __name__ == '__main__':
    train_data = get_csv_data('titanic3_train.csv')
    test_data = get_csv_data('titanic3_test.csv')
    
    missing_data_calc = HandleMissingData(train_data, test_data)
    
    train_data = missing_data_calc.get_fixed_train_data()
    test_data = missing_data_calc.get_fixed_test_data()

    queries = Queries(train_data)

    # Get all different enumerators of the table sex
    gender_types = queries.get_column_values(train_data, 'sex')
    # Get all different enumerators of the table class
    pclass_types = queries.get_column_values(train_data, 'pclass')

    # Add a column zSex with the related index of gender_types
    train_data = queries.add_attribute(train_data, 'sex', 'zSex', gender_types)
    # Add a column zPClass with the related index of pclass
    train_data = queries.add_attribute(train_data, 'pclass', 'zPclass', pclass_types)
    
    
    train_data = queries.add_age_group(train_data, 'age', 'zAge')
    zAge_types = queries.get_column_values(train_data, 'zAge')

    # For every pClass compute 4 different ticket ranges
    pclasses_dict = queries.group_by_attribute(train_data, 'pclass')
    fare_breaks_pclass = {i: queries.get_groups_of_attribute(y, 'fare', 4) for i, y in pclasses_dict.items()}
    
     
    # Add the new range class to the train_data in the column zFare_per_pclass
    train_data = queries.add_group_attribute(train_data, 'pclass', 'fare', 'zFare_per_pclass', fare_breaks_pclass)

    # Create an empty survival table
    survival_table = np.zeros((len(gender_types), len(pclass_types), 
        len(fare_breaks_pclass['1']), max(zAge_types) + 1))
    
    # Assign every passenger to a new dictionary ''grouped_values'', where the key represents their group
    # --> see method get_key
    grouped_values = {}
    for entry in train_data:
        key = get_key(entry)
        if key not in grouped_values:
            grouped_values[key] = np.array(entry)
        else:
            grouped_values[key] = np.append(grouped_values[key], entry)
    
    # find The Proportion of Survival for every group
    for j in grouped_values.values():
        index = j.item(0)['zSex'], j.item(0)['zPclass'], j.item(0)['zFare_per_pclass'], j.item(0)['zAge']
        survival_table[index] = queries.proportion_of_survival(j)

    # Take the group from the training data and assign them to the test
    test_data = queries.add_attribute(test_data, 'sex', 'zSex', gender_types)
    test_data = queries.add_attribute(test_data, 'pclass', 'zPclass', pclass_types)
    test_data = queries.add_group_attribute(test_data, 'pclass', 'fare', 'zFare_per_pclass', fare_breaks_pclass)
    test_data = queries.add_age_group(test_data, 'age', 'zAge')
    
    output_data = []
    for j in test_data:
        index = j['zSex'], j['zPclass'], j['zFare_per_pclass'], j['zAge']
        age = 100
        try: 
            age = float(j['age'])
        except:
            pass
        if survival_table[index] >= 0.5:
            output_data.append([j['id'], 1])
        else: 
            output_data.append([j['id'], 0])

    write_csv_data('test_submission.csv', output_data)

    file = open('test_submission.csv')
    urlstring = 'https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/titanic.html?submission=wolfensberger_test_6&csv='
    urlrequest = urlstring + urllib.parse.quote(file.read())
    urllib.request.urlopen(urlrequest)

    # age in survival table?
# address https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/titanic.html


    
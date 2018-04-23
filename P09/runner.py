from titanicdata.src import Queries, get_csv_data, write_csv_data, HandleMissingData
import numpy as np

if __name__ == '__main__':
    train_data = get_csv_data('titanic3_train.csv')
    test_data = get_csv_data('titanic3_test.csv')
    
    missing_data_calc = HandleMissingData(train_data, test_data)
    
    train_data = missing_data_calc.get_fixed_train_data()
    test_data = missing_data_calc.get_fixed_train_data()

    queries = Queries(train_data)


    train_data = queries.add_attribute(train_data, 'sex', 'zSex')
    train_data = queries.add_attribute(train_data, 'pclass', 'zPclass')

    pclasses_dict = queries.group_by_attribute(train_data, 'pclass')
    fare_breaks_pclass = {i: queries.get_groups_of_attribute(y, 'fare', 4) for i, y in pclasses_dict.items()}
    
    train_data = queries.add_group_attribute(train_data, 'pclass', 'fare', 'zFare_per_pclass', fare_breaks_pclass)

    survival_table = np.zeros((
        len(np.unique(queries.get_column_values(train_data, 'zSex'))), 
        len(np.unique(queries.get_column_values(train_data, 'zPclass'))), 
        len(fare_breaks_pclass['1'])))
    


    """
    """

    #gender_pclass_fares = {i: queries.group_by_attribute(y, 'fare', fare_breaks_pclass[i]) for i, y in pclasses.items()}
    


    """ gender_proportions = queries.proportion_gender_survival()



    output_data = []
    for entry in test_data:
        if (entry['sex'] == 'female'):
            output_data.append([entry['id'], 1])
        else: 
            output_data.append([entry['id'], 0])

    write_csv_data('test_submission.csv', output_data) """

# address https://openwhisk.ng.bluemix.net/api/v1/web/ZHAW%20ISPROT_ISPROT17/default/titanic.html

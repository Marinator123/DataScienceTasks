from titanicdata.src import Queries, get_csv_data, write_csv_data

if __name__ == '__main__':
    train_data = get_csv_data('titanic3_train.csv')
    queries = Queries(train_data)
    gender_proportions = queries.proportion_gender_survival()

    test_data = get_csv_data('titanic3_test.csv')

    output_data = [['100001', '0'], ['100002', '1']]
    write_csv_data('test_submission.csv', output_data)




#np.sum([int(d['survived']) for d in bla])
#[d for d in bla if d['sex'] == 'female']

#x = np.random.randn(20, 3)
#x_new = x[np.sum(x, axis=1) > .5]

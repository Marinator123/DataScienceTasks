class HandleMissingData:
    def __init__(self, train_data, test_data):
        self.train_data = train_data
        self.test_data = test_data
        self.mean_fare_per_class = self.calculate_mean_fare_per_class()
        train_data = self.fill_missing_fares(train_data)
        test_data = self.fill_missing_fares(test_data)
        

    def get_fixed_train_data(self):
        return self.train_data

    def get_fixed_test_data(self):
        return self.test_data

    def calculate_mean_fare_per_class(self):
        sum_and_number_of_fares_per_class = {}
        for entry in self.train_data:
            pclass = entry['pclass']
            try:
                fare = float(entry['fare'])
                if fare == 0:
                    continue
                if (sum_and_number_of_fares_per_class.get(pclass) == None):
                    sum_and_number_of_fares_per_class[pclass] = [1, fare]
                else:
                    temp_entry = sum_and_number_of_fares_per_class[pclass]
                    sum_and_number_of_fares_per_class[pclass] = [temp_entry[0]+1, temp_entry[1]+fare]
            except ValueError:
                continue

        mean_fare_per_class = {}
        for pclass, values in sum_and_number_of_fares_per_class.items():
            if (values[0] > 0):
                mean_fare_per_class[pclass] = values[1] / values[0]
        return mean_fare_per_class

    def fill_missing_fares(self, data):
        for entry in data:
            fare = 0
            try:
                fare = float(entry['fare'])
            except ValueError:
                pass
            if fare == 0:
                entry['fare'] = self.mean_fare_per_class[entry['pclass']]
        return data
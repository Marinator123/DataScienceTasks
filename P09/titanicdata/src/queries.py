import numpy as np 


class Queries:
    def __init__(self, data):
        self.data = data

    def proportion_of_survival(self, data):
        if (np.size(data) == 1):
            return int(data.item(0)['survived'])
        num_survived = np.size(list(filter(lambda x: int(x['survived']), data)))
        return num_survived / len(data)
    
    def group_by_attribute(self, data, column, groups = None):
        grouped_data = {}
        for entry in data:
            attribute_value = entry[column]
            if (groups != None): # gruppieren von zahlen
                attribute_value = float(attribute_value)
                for i in range(0, len(groups)):
                    if (attribute_value <= groups[i]):
                        attribute_value = i
                        break
            if (grouped_data.get(attribute_value) == None):
                grouped_data[attribute_value] = [entry]
            else:
                grouped_data[attribute_value].append(entry)
        return grouped_data

    def add_attribute(self, data, column, name_attribute, types):
        for entry in data:
            attribute_value = entry[column]
            for i in range(0, len(types)):
                if (attribute_value == types[i]):
                    attribute_value = i
            entry[name_attribute] = attribute_value
        return data

    def add_group_attribute(self, data, group_column, value_column, name_attribute, groups):
        for entry in data:
            group_values = groups[entry[group_column]]
            attribute_value = float(entry[value_column])
            for i in range(0, len(group_values)):
                if (attribute_value <= group_values[i]):
                    attribute_value = i
                    break
            entry[name_attribute] = attribute_value
        return data

    def get_groups_of_attribute(self, data, column, number_of_groups):
        len_data = len(data)
        column_array = np.zeros(len_data)
        for i in range(len_data):
            column_array[i] = data[i][column]
        column_array.sort()
        column_array = np.array_split(column_array, number_of_groups)

        return [y.max() for y in column_array]

    def get_column_values(self, data, column_name):
        column_values = []
        for i in range(0, len(data)):
            if (data[i][column_name] not in column_values):
                column_values.append(data[i][column_name])
        return column_values

    def add_age_group(self, data, column, name_attribute):
        for entry in data:
            attribute_value = entry[column]
            age_group = -1
            if (attribute_value == ''):
                age_group = 0
            elif (float(attribute_value) < 14):
                age_group = 1
            else:
                age_group = 2
            entry[name_attribute] = age_group
        return data
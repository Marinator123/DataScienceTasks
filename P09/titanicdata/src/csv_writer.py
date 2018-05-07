import csv

def write_csv_data(filename, data):
    with open(filename, 'w', newline='') as f:
        file_object = csv.writer(f, delimiter=';')
        file_object.writerow(get_header())
        for row in data:
            file_object.writerow(row)

def get_header():
    return (['key', 'value'])

# Testrunner
if __name__ == '__main__':
    data = [['100001', '0'], ['100002', '1']]
    write_csv_data(r'./test.csv', data)
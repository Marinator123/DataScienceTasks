from xlrd import open_workbook

def read_excel(filename):
    try:
        with open_workbook(filename, 'r') as book:
            sheet_dict = {}
            for sheet in book.sheets():
                dict_list = read_sheet(sheet)
                sheet_dict[sheet.name] = dict_list
            return sheet_dict
    except FileNotFoundError:
        print("File %s not found" % (filename))

def read_sheet(sheet):
    # get header columns
    keys = [sheet.cell(0, col_index).value for col_index in range(sheet.ncols)]
    dict_list = []
    # get all rows
    for row_index in range(1, sheet.nrows):
        d = {keys[col_index]: sheet.cell(row_index, col_index).value for col_index in range(sheet.ncols)}
        dict_list.append(d)
    return dict_list

if __name__ == '__main__':
    read_excel('p08_hockey_stats.xlsx')
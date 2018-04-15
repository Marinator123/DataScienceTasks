import unittest

class TestExcel(unittest.TestCase):
    def test_read_excel(self):
        dict_result = read_excel('../../p08_hockey_stats.xlsx')
        self.assertEqual(dict_result['Davos'] != None, True)

if __name__ == '__main__':
    import sys
    from os.path import dirname, abspath
    d = dirname(dirname(dirname(abspath(__file__))))
    sys.path.append(d)
from numpyexample.src import read_excel
unittest.main()
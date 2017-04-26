import ntpath
import urllib3
import certifi
import os
from HW4 import get_data
from HW4 import remove_data
from HW4 import path_leaf
import unittest

class Test_get_data(unittest.TestCase):

    #Test case 1: file is not present locally, and the URL points to a file that exists
    def test_get_case_1(self):
        url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        filename = path_leaf(url)
        self.assertFalse(os.path.exists(filename))
        get_data(url)
        self.assertTrue(os.path.exists(filename))
        remove_data(url)

    #Test case 2: file is present locally
    def test_get_case_2(self):
        url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        filename = path_leaf(url)
        get_data(url)
        self.assertTrue(os.path.exists(filename))
        remove_data(url)

    #Test case 3: URL does not point to a file that exists.
    def test_get_case_3(self):
        t3 = get_data('https://data.seattle.gov/resource/4xy.csv')
        self.assertEqual(t3, 404)


if __name__ == '__main__':
    unittest.main()

import ntpath
import urllib3
import certifi
import os
from HW4 import get_data
from HW4 import remove_data
from HW4 import path_leaf
import unittest

class Test_remove_data(unittest.TestCase):

    #Test case 1: file is not present locally
    def test_remove_case_1(self):
        url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        filename = path_leaf(url)
        remove_data(url)
        self.assertFalse(os.path.exists(filename))

    #Test case 2: file is present locally
    def test_remove_case_2(self):
        url = 'https://data.seattle.gov/resource/4xy5-26gy.csv'
        filename = path_leaf(url)
        get_data(url)
        self.assertTrue(os.path.exists(filename))
        remove_data(url)
        self.assertFalse(os.path.exists(filename))

if __name__ == '__main__':
    unittest.main()

'''
    File Name: HW04VigneshMohan (test).py
    Script Author: Vignesh Mohan
    Purpose: Week 4 Assignment.
    Python Version: 3.0
'''

'''Test Code for developing with the perspective of a tester in mind'''

import unittest

from HW04VigneshMohan import get_user_information

class Test(unittest.TestCase):
    def test_gitRepo(self):
       
        expected = ['User Name in Github: Vigzm1995',
                    'Repository: CS-546 Number of commits inside the repository: 30',
                    'Repository: shift-sleeping-barber-problem Number of commits inside the repository: 2',
                    'Repository: SSW-567 Number of commits inside the repository: 16',
                    'Repository: SSW-810 Number of commits inside the repository: 6',
                    'Repository: SSW690-project Number of commits inside the repository: 8']

        self.assertEqual(get_user_information(), expected)

    def test_bad_user_name(self):
        self.assertEqual(get_user_information('aaaabbbbcccc'), 'unable to fetch repos from user')
        self.assertEqual(get_user_information(''), 'unable to fetch repos from user')

if __name__ == '__main__':
    unittest.main()

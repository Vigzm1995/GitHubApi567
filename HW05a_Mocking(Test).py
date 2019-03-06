from HW05a_Mocking import numCommits, repoList
import unittest
from unittest.mock import Mock, patch


class Test04(unittest.TestCase):
    @patch('requests.get')
    def test_repoList(self, mock_get):
            repojson = [{
                'name': 'TestRepo'}
            ]
            #mock_get.return_value = repojson
            mock_get.return_value.json.return_value = repojson
            response = repoList('Guy')
            self.assertEqual(response, ['TestRepo'])

    @patch('requests.get')    
    def test_numCommits(self, mock_get):
            repocommits = [{
                '0': {'commit': '1'}
            },
                {'1': {'commit': '2'}
            },

                {'2': {'commit': '3'}
            },
                {'3': {'commit': '4'}
            }

            ]
            mock_get.return_value.json.return_value = repocommits
            response = numCommits('Test', 'Also Test')
            self.assertEqual(response, 4)
            

if __name__ == "__main__":
    print('Running unit tests...')
    unittest.main()
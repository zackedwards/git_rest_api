import json
import unittest

from unittest.mock import Mock, patch
from git_repo import get_info

class Test_get_info(unittest.TestCase):

    def test_my_git(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value = True
            response=get_info('zackedwards')
            self.assertTrue(response)

    

    def test_not_a_real_git(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value = False
            self.assertFalse(get_info('pleasedontexist'))

if __name__ == '__main__':
    unittest.main()
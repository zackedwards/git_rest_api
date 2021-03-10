import requests
import json
import unittest

def get_info(name):
    try:
        user = requests.get('https://api.github.com/users/{ID}/repos'.format(ID=name))
        data = user.json()

        for i in data:
            repo = i['name']
            repo_url = 'https://api.github.com/repos/zackedwards/{REPO}/commits'.format(REPO=repo)
            repo_response = requests.get(repo_url)
            repo_data = repo_response.json()
            counter=0
            for j in repo_data:
                counter+=1
            print('Repo:', repo, 'Number of commits:', counter)
        return True
    except:
        return False
class Test_get_info(unittest.TestCase):

    def test_my_git(self):
        self.assertTrue(get_info('zackedwards'))
    
    def test_not_a_real_git(self):
        self.assertFalse(get_info('pleasedontexist'))

if __name__ == '__main__':
    unittest.main()
import requests

def get_info(name):
    try:
        data = user_api(name)
        for i in data:
            repo_data=repo_api(i)
            repo = i['name']
            counter=0
            for j in repo_data:
                counter+=1
            print('Repo:', repo, 'Number of commits:', counter)
        return True
    except:
        user_data=requests.get('https://api.github.com/users/{ID}/repos'.format(ID=name))
        if user_data:
            return True
        return False
def user_api(name):
    user = requests.get('https://api.github.com/users/{ID}/repos'.format(ID=name))
    data = user.json()
    return data
def repo_api(i):
    repo = i['name']
    repo_url = 'https://api.github.com/repos/zackedwards/{REPO}/commits'.format(REPO=repo)
    repo_response = requests.get(repo_url)
    repo_data = repo_response.json()
    return repo_data
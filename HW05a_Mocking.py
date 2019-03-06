import requests

def repoList(id):
    repoArr = []
    r = requests.get('https://api.github.com/users/{}/repos'.format(id))
    repoList = r.json()
    for line in repoList:
        repo = line.get('name')
        repoArr.append(repo)
    return repoArr

def numCommits(id, repo):
    r =requests.get('https://api.github.com/repos/{}/{}/commits'.format(id, repo))
    commits = r.json()
    return len(commits)


def HW04():
    id = input("What is the github username?\n")
    listofRepos = repoList(id)
    for repo in listofRepos:
        num = numCommits(id, repo)
        print ("Repo: {}\nCommits: {}".format(repo, num))

if __name__ =="__main__":
    HW04()
    
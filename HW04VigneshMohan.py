'''
    File Name: HW04VigneshMohan.py
    Script Author: Vignesh Mohan
    Purpose: Week 4 Assignment.
    Python Version: 3.0
'''

'''Program for developing with the perspective of a tester in mind'''

#Importing 'requests' module to make and handle requests
import requests
#Importing 'json' module to parse the JSON repo_response data from the github API 
import json
#Importing 'urllib.parse' module to parse the URL's.
import urllib.parse
#Importing the 'urllib.error' module to rectify invalid user's URL input.
import urllib.error

def get_user_information():

    '---------- CODE FOR GETTING THE NUMBER OF REPOSITORIES ----------'

    #Getting the User's Input.    
    username = 'Vigzm1995'
    #type('Vigzm1995')
    #Initializing 'return_result' as an empty list.
    return_result = []
    #Retrieving a user's repositories from Github.
    api_url = 'https://api.github.com/users/{}/repos'.format(username)
    #Reading the data from the github repository.
    res= requests.get(api_url)
     #Using the '.loads' option in-built to parse the returned JSON in a text format.
    repo_data = json.loads(res.text)
    #Returning the user's data read from Github in a formatted method and append the same.
    return_result.append('User Name in Github: {}'.format(username))
    try:
        repo_data[0]['name']
    except urllib.request.URLError:
        print("The URL is incorrect. Please Enter the Correct Error.")
        return
    
    '---------- CODE FOR GETTING THE NUMBER OF COMMITS WITHIN EACH REPOSITORY ----------'

    try:
        #Usage for for loop as all the commits to be searched need to be from the 'for' loop from the repository.
        for repository in repo_data:
            #Accessing the repository name and returning it as a JSON object.
            repository_name = repository['name']
            #Retrieving a user's commit from the repositories from Github.
            commit_url = 'https://api.github.com/repos/{}/{}/commits'.format(username, repository_name)
            #Reading the data from the github repository.
            repository_info = requests.get(commit_url)
            #Using the '.loads' option in-built to parse the returned JSON in a text format.
            repo_data1 = json.loads(repository_info.text)
            #Returning the user's data read from Github in a formatted method and append the same by returing the length of the json object.
            return_result.append('Repository: {} Number of commits inside the repository: {}'.format(repository_name, len(repo_data1)))

    #Expect function to check for invalid inputs.
    except (TypeError):
        return 'Cannot get commmits'
    return return_result

#Invoking the main function that in-turn invokes the 'get_user_information' function.
if __name__ == '__main__':
    #Checking for the result of the JSON objects that are fetched using the github API and printing the same.
     for data_fetched in get_user_information():
        print(data_fetched)


        

        

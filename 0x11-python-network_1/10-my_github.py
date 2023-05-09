#!/usr/bin/python3
"""
Takes your GitHub credentials(username and password)
utilizes the GitHub API and displays id
"""

from sys import argv
from requests import get
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    api = 'https://api.github.com/user'
    request = get(api, auth=HTTPBasicAuth(argv[1], argv[2]))
    print(request.json().get('id'))

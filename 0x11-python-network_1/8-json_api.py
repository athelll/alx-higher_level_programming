#!/usr/bin/python3
"""
Takes a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the
letter as a parameter.
"""

import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        payload = {'q': ''}
    else:
        payload = {'q': sys.argv[1]}

    # request and response
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    try:
        r = response.json()
        if r:
            print('[{}] {}'.format(r.get('id'), r.get('name')))
        else:
            print("No result")
    except ValueError:
        print('Not a valid JSON')

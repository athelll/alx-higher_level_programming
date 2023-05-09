#!/usr/bin/python3
"""
Sends request to a URL and displays
the body of the response (decoded in utf-8)
handles prints error code if ant arises
"""

import sys
import urllib.request as request
from urllib.error import HTTPError

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code: {}'.format(error.code))

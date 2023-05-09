#!/usr/bin/python3
"""
Sends a request to a URL and
displays the value of the variable `X-Request-Id`
in the response header using `requests` package
"""

import sys
import requests

if __name__ == '__main__':
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))

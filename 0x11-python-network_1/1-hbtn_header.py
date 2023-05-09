#!/usr/bin/python3
"""
sends a request to the URL and
displays the value of the X-Request-Id variable
in responses header
"""

import sys
import urllib.request as request

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])

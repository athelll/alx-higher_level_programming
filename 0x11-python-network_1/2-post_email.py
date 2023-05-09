#!/usr/bin/python3
"""
sends a POST request to the passed URL
with the email as a parameter
and displays the body of the response (decoded in utf-8)
"""

import sys
import urllib.request as request
import urllib.parse as parse

if __name__ == '__main__':
    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = parse.urlencode(value)
    data = data.encode('ascii')
    post_request = request.Request(url, data)

    with request.urlopen(post_request) as response:
        print(response.read().decode('utf-8'))

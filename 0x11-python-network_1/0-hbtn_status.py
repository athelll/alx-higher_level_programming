#!/usr/bin/python3
"""
Python script that fetches response 
from `https://alx-intranet.hbtn.io/status`
"""

import urllib.request

if __name__ == "__main__":
    # function doesnt run when imported
    url = "https://alx-intranet.hbtn.io/status"
    opener = urllib.request.urlopen

    with opener(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

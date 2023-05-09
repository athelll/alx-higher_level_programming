#!/usr/bin/python3
"""
Python script that fetches response
from `https://alx-intranet.hbtn.io/status`
"""

if __name__ == "__main__":
    # code does'nt execute when imported

    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"
    opener = urllib.request.urlopen

    with opener(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))

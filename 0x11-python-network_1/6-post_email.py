#!/usr/bin/python3
"""
Sends a POST request to the passed URL
with the email as a parameter and displays the
body of the response using requests
"""

import sys
import requests

if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=payload)
    print(response.text)

#!/bin/bash
# sends a DELETE request to a URL passed as first argument and displays the body of the response
curl -sX DELETE "$1"

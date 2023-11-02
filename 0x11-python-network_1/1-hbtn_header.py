#!/usr/bin/python3
"""
This module takes in a URL, sends a request to the URL & displays the
X-Request-Id variable found in the header of the response
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))
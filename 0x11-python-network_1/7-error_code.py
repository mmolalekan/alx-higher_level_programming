#!/usr/bin/python3
"""This module fetches https://alx-intranet.hbtn.io/status"""
import requests
import sys

url = sys.argv[1]
r = requests.get(url)
if r.status_code >= 400:
    print("Error code:", r.status_code)
else:
    print(r.text)


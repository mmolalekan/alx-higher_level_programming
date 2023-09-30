#!/usr/bin/python3
import requests
"""This module fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

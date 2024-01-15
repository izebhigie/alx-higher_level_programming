#!/usr/bin/python3
""" This python script uses the username and password of the client
to get the client's GitHub userID
Usage: ./<python script> <GitHub username> <GitHub password>
  - Get ID using basic authentication
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

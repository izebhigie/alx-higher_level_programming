#!/usr/bin/python3
""" This python script sends the email parameter to a URL using the POST method
and the request and sys libraries
Usage: ./<python script> <URL> <email>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    r = requests.post(url, data=value)
    print(r.text)

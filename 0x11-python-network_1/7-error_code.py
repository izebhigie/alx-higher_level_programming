#!/usr/bin/python3
""" This python script handles errors from URL requests
using requests and sys libraries
Usage: ./<python script> <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)

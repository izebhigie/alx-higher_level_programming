#!/usr/bin/python3
""" This python script gets the X-request-Id of a URL response using request library
Usage: ./<Python script> <URL>
"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    print(r.headers.get("X-Request-Id"))

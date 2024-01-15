#!/usr/bin/python3
"""This python script gets the x-request-ID header from the given URL response
Usage: ./<python script>  <URL>
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        print(dict(response.headers).get("X-Request-Id"))

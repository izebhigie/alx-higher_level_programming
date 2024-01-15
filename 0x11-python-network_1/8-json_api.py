#!/usr/bin/python3
""" This python script sends a letter to http://0.0.0.0:5000/search_user using the POST method
Usage: ./<python script> <letter>
  - The letter sent belongs to the variable q
  - Handle the situation when no letter is provided
"""
import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")

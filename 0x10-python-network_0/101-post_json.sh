#!/bin/bash
# This script passes a JSON filetype to a URL using the POST method and gets the body of the response
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"

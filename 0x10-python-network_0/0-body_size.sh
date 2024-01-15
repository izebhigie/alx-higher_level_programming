#!/bin/bash
# This script sends a request for the size of the body of the response got from a URL
curl -s "$1" | wc -c

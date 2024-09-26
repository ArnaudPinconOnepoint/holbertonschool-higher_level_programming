#!/usr/bin/python3
"""
1-hbtn_header

This module takes a URL as a command-line argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header of the response test.
"""

import urllib.request
import sys

def fetch_request_id(url):
    """Fetches and displays the value of the X-Request-Id header from a given URL."""
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        headers = response.info()
        request_id = headers.get('X-Request-Id')
        if request_id:
            print(request_id)
        else:
            print('No X-Request-Id header found')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
    else:
        fetch_request_id(sys.argv[1])

#!/usr/bin/python3
"""
3-error_code.py

This module fetches and displays the status of a website.
"""

import urllib.request
import sys

def fetch_status(url):
    """Fetches and displays the status of a website."""
    try: 
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            body = response.read()
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        return

    print("Body response:")
    print(f"    - type: {type(body)}")
    print(f"    - content: {body}")
    print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <URL>")
    else:
        fetch_status(sys.argv[1])

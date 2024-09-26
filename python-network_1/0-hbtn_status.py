#!/usr/bin/python3
"""
0-hbtn_status

This script fetches the status of a website using urllib.
"""

import urllib.request


def fetch_status():
    """Fetches and displays the status of a website."""
    url = 'https://intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()

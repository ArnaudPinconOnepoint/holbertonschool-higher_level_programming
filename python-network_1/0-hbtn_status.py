#!/usr/bin/python3
"""
0-hbtn_status

This script fetches the status of a website using urllib with a User-Agent header.
"""

import urllib.request

def fetch_status():
    """Fetches and displays the status of a website."""
    url = 'https://intranet.hbtn.io/status'
    user_agent = 'Mozilla/5.0 (Linux x86_64)'  # Common user-agent

    # Create a request object with the user-agent header
    request = urllib.request.Request(url, headers={'User-Agent': user_agent})

    # Use a with statement to manage the request
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()

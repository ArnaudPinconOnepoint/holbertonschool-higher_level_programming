#!/usr/bin/python3
"""
0-hbtn_status

This script fetches the status of a website using urllib with a User-Agent header.
It displays the type, content, and utf-8 decoded content of the response.
"""

import urllib.request

def fetch_status():
    """
    Fetches and displays the status of a website.
    
    The function sends a GET request to the Holberton intranet
    and prints the response body with proper formatting.
    """
    url = 'https://intranet.hbtn.io/status'
    
    # User-Agent header using get method for dictionary access
    headers = {'User-Agent': 'HolbertonSchool-Checker'}

    # Create a request object
    request = urllib.request.Request(url, headers=headers)

    # Use a with statement to handle the request
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()

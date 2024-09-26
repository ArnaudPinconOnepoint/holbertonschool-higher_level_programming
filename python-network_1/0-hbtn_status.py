#!/usr/bin/python3
"""
0-hbtn_status

This script fetches the status of a website using urllib with a User-Agent header.
It displays the type, content, and utf-8 decoded content of the response.
"""

import urllib.request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    
    # User-Agent header using get method for dictionary access
    headers={"User-agent": "Mozilla/5.0 (Linux x86_64)"}

    # Create a request object
    request = urllib.request.Request(url, headers=headers)

    # Use a with statement to handle the request
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

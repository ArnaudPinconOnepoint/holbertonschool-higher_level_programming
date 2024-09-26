#!/usr/bin/python3
"""
0-hbtn_status

This script fetches the status of a website
using urllib with a User-Agent header.
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    # headers = {"User-Agent": "Mozilla/5.0 (Linux x86_64)"}
    # request = urllib.request.Request(url, headers)
    with urllib.request.urlopen(urllib.request.Request(url)) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")

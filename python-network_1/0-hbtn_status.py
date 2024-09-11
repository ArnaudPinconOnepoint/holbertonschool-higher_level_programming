#!/usr/bin/python3
"""
0-hbtn_status

This module fetches and displays the status of a website.
"""

import urllib.request

def fetch_status():
    """Fetches and displays the status of a website."""
    url='https://intranet.hbtn.io/status'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    with urllib.request.urlopen(url) as response:
       body = response.read()
       print("Body response:")
       print(f"    - type: {type(body)}")
       print(f"    - content: {body}")
       print(f"    - utf8 content: {body.decode('utf-8')}")

if __name__ == "__main__":
    fetch_status()

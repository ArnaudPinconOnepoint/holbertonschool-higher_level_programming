#!/usr/bin/python3
"""
1-hbtn_header

This module takes a URL as a command-line argument, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

def send_email(url, email):
    """Fetches and displays the value of the X-Request-Id header from a given URL."""
    value = { "email": email}
    data = value.encode('utf-8')  # data should be bytes
    req = urllib.request.Request(url, data, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./1-hbtn_header.py <URL>")
    else:
        send_email(sys.argv[1], sys.argv[2])

#!/usr/bin/python3
"""

This module fetches and displays the status of a website.
"""

import urllib.request


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
    print(f"    - content: {body.decode('utf-8')}")


if __name__ == "__main__":
    fetch_status("https://intranet.hbtn.io/status")


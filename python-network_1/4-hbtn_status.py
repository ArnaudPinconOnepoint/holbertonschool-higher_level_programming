#!/usr/bin/python3
"""

This module fetches and displays the status of a website.
"""

import requests


def fetch_status(url):
    """Fetches and displays the status of a website."""
    try:
        r = requests.get(url)
    except requests.exceptions as e:
        print(f"Error code: {e.code}")
        return

    print("Body response:")
    print(f"    - type: {type(r.text)}")
    print(f"    - content: {r.status_code}")


if __name__ == "__main__":
    fetch_status("https://intranet.hbtn.io/status")


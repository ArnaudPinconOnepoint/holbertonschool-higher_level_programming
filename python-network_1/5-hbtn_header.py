#!/usr/bin/python3
"""

This module fetches and displays the status of a website.
"""

import requests
import sys


def fetch_status(url):
    """Fetches and displays the status of a website."""
    try:
        r = requests.get(url)
    except requests.exceptions as e:
        print(f"Error code: {e.code}")
        return

    print(r.headers.get("X-Request-Id"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You need <URL>")
    else:
        fetch_status(sys.argv[1])

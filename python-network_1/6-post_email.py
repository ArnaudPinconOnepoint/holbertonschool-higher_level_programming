#!/usr/bin/python3
"""

This module fetches and displays the status of a website.
"""

import requests
import sys


def fetch_network(url, email):
    """Fetches and displays the status of a website."""
    try:
        r = requests.post(url, data={'email': email})
    except requests.exceptions as e:
        print(f"Error code: {e.code}")
        return

    print(r.text)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You need <URL>")
    else:
        fetch_network(sys.argv[1], sys.argv[2])

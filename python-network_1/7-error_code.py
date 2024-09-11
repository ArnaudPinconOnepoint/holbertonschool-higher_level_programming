#!/usr/bin/python3
"""

This module fetches and displays the status of a website.
"""

import requests
import sys


def fetch_network(url):
    """Fetches and displays the status of a website."""
    try:
        r = requests.get(url)
        print(r.content.decode("utf-8"))
    except requests.exceptions as e:
        print(f"Error code: {r.status_code}")
        return

    print(r.content.decode("utf-8"))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("You need <URL>")
    else:
        fetch_network(sys.argv[1])

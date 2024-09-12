#!/usr/bin/python3
"""

This module fetches and displays the body of the response
from a URL and check if there is an error.
"""

import requests
import sys


def fetch_network(url):
    """Fetches and displays the body of the response from a URL."""
    try:
        r = requests.get(url)
        # Check if the HTTP status code is greater than or equal to 400
        if r.status_code >= 400:
            print(f"Error code: {r.status_code}")
        else:
            # Print the content of the response (body)
            print(r.content.decode("utf-8"))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    fetch_network(sys.argv[1])

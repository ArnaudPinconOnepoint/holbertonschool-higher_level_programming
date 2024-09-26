#!/usr/bin/python3
"""
This module sends a POST request with a
letter parameter to a specific URL
and processes the JSON response to display
the user id and name or appropriate error messages.
"""

import requests
import sys


def fetch_network(letter=""):
    """Fetches data from the network and processes the res"""
    try:
        r=requests.post("http://0.0.0.0:5000/search_user", data={'q': letter})
        r.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    try:
        response_json = r.json()  # Parse the JSON response
    except ValueError:
        print("Not a valid JSON")
        return

    if not response_json:
        print("No result")
        return

    try:
        user_id = response_json['id']
        user_name = response_json['name']
        print(f"[{user_id}] {user_name}")
    except KeyError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("You need one parameter")
    else:
        letter = sys.argv[1] if len(sys.argv) == 2 else ""
        fetch_network(letter)

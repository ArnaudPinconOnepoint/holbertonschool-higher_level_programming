#!/usr/bin/python3
"""
This module uses GitHub API with Basic
Authentication to display the user ID
based on provided GitHub credentials
(username and personal access token).
"""


import requests
import sys

def fetch_github_user_id(username, token):
    """Fetches the GitHub user ID using Basic Authentication."""
    try:
        response = requests.get(
            "https://api.github.com/user",
            auth=(username, token)
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

    try:
        user_info = response.json()
        user_id = user_info.get('id')
        if user_id:
            print(f"User ID: {user_id}")
        else:
            print("User ID not found")
    except ValueError:
        print("Error: Response is not valid JSON")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <username> <personal_access_token>")
    else:
        username = sys.argv[1]
        token = sys.argv[2]
        fetch_github_user_id(username, token)

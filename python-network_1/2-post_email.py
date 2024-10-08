#!/usr/bin/python3
"""
script that takes in a URL and an email
sends a POST request to the passed URL with the email as a parameter
and displays the body of the response toto
"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    body = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(body).encode("ascii")

    request = urllib.request.Request(url, data=data, method="POST")
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))

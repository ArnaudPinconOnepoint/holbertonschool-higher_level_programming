#!/usr/bin/python3
"""
0-hbtn_status

This module checks the status of a website.
"""

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()

print(html.decode('utf-8'))

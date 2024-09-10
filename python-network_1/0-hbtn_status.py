#!/usr/bin/python3
"""
0-hbtn_status

This module check the status of a website

"""

import urllib.request
with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
   html = response.read()

#!/usr/bin/env python3

import sys
import requests

def main():
    # get IP location from IP API - https://ipapi.co/
    response = requests.get('https://ipapi.co/json')
    latitude = response.headers.get('latitude')
    longitude = response.headers.get('longitude')
    return latitude, longitude

try:
  main()
except:
  sys.exit(1)

sys.exit(0)

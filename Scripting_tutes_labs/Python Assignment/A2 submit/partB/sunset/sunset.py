#!/usr/bin/env python3

import sys
import requests

def main():

    # get IP location from IP API - https://ipapi.co/
    response = requests.get('https://ipapi.co/json')
    latitude = response.headers.get('latitude')
    longitude = response.headers.get('longitude')

    # and get rise and set data about the location proviced thanks to https://api.sunrise-sunset.org
    RiseSetURL = "api.sunrise-sunset.org/json?lat=" + str(latitude) + "&lng=" + str(longitude)
    response = requests.get('https://' + RiseSetURL)
    sunset = response.headers.get('sunset')
    print(sunset)

try:
  main()
except:
  sys.exit(1)

sys.exit(0)

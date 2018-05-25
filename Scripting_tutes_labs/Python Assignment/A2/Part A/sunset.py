#!/usr/bin/env python3

import sys
import time
import requests

def main(latitude, longitude):
    timezone = time.strptime(str(time.localtime()),'%z')
    RiseSetURL = "api.sunrise-sunset.org/json?lat=" + latitude + "&lng=" + longitude
    response = requests.get('https://' + RiseSetURL)
    sunset = response.headers.get('sunset')
    return sunset

try:
  main()
except:
  sys.exit(1)

sys.exit(0)

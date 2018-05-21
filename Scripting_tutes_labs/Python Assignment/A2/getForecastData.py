#!/usr/bin/env python3

# Documentation for the requests system
# http://docs.python-requests.org/en/master/

# To access forecasts you'll need a forecast.io account (free)
# This will give you an API key that you use in each call

import requests
import json			# so we can decode the response
import sys
import re
from pathlib import Path

# get IP location from IP API - https://ipapi.co/
def getLocation():
    response = requests.get('https://ipapi.co/json')
    latitude = response.headers.get('latitude')
    longitude = response.headers.get('longitude')
    timezone = response.headers.get('utc_offset')
    return latitude, longitude, timezone

# request forecast from Dark Sky API - https://darksky.net/dev/
def getForecast(forecastURL, apikey, latitude, longitude, options):
    path = "/forecast/" + apikey + "/" + latitude + "," + longitude  + options
    response = requests.get('https://' + forecastURL + path)
    data = response.text
    return json.loads(data)

# Challenge: Sunrise and Sunset times as provided by the free API found at https://sunrise-sunset.org/api
def getRiseSetTimes(riseSetURL):
    response = requests.get('https://' + RiseSetURL)
    data = response.text
    return json.loads(data)
# TO DO - Convert from UTC to time zone of location.

def main():

    # identification of an existing config file in json format in the first command line argument after
    p = re.compile('\S+\.json')

    for i in sys.argv():
        re.match(p,i)
        if(match):
            try:
                file = Path(i)
                if file.is_file():
                    config = i
                    break
        else:
            config = './ifttt.json'

    # mandatory fields are name, program and description
    

	# Get the API key

	# It can be stored in the configuration file (recommended option for this program)
	# You would then read it from the command line arguments


	# I've placed it in a file because I don't want you to see it!
    with open(".env") as file:
    	apiKey = file.readline().strip()

    RiseSetURL = "api.sunrise-sunset.org/json?lat=" + latitude + "&lng=" + longitude

    forecastURL = "api.forecast.io"

    forecast = getForecast(forecastURL, apiKey, latitude, longitude, '')

    print (str(forecast))



main()

sys.exit(0)

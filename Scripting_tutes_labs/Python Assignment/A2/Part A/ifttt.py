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
    return latitude, longitude, sys.exit(0)

def main(argv):

    # identification of an existing config file in json format in the first command line argument after
    p = re.compile('\S+\.json')

    for i in sys.argv[i]:
        re.match(p,i)
        if(match):
            file = Path(i)
            if file.is_file():
                config = i
                break
        else:
            config = './ifttt.json'

    # mandatory fields are name, program and description
#    for service in config:
        # check json for the headers...

	# Get the API key

	# It can be stored in the configuration file (recommended option for this program)
	# You would then read it from the command line arguments


	# I've placed it in a file because I don't want you to see it!
#    with open(".env") as file:
#    	apiKey = file.readline().strip()



    # do more stuff here...
#    print (str(time)) #################################### !!!!!!!

if __name__ == "__main__":
    main(sys.argv[1:])

sys.exit(0)

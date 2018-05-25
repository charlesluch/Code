#!/usr/bin/env python3

# Documentation for the requests system
# http://docs.python-requests.org/en/master/

import requests
import json			# so we can decode the response
import sys
import re
from pathlib import Path


# your program is driven by the json file, which defines what things have to happen.
# you read the file and see "ah, I have to kick off the action to get the date, then get the output from that, and feed it into the next thing to be run. I'll keep doing that until the workflow is complete, or tells me to stop."

def main(argv):

    # identification of an existing config file in json format in the first command line argument after
    p = re.compile('\S+\.json')
    config = ''
    output = ''

    try:
        opts, args = getopt.getopt(argv,)
    for i in sys.argv[i]:
        re.match(p,i)
        if(match):
            file = Path(i)
            if file.is_file():
                config = i
                break
        else:
            config = './ifttt.json'

    with open(config) as c:
        plan = json.load(c)

        for# check json for the headers...


	# Get the API key

	# It can be stored in the configuration file (recommended option for this program)
	# You would then read it from the command line arguments


	# I've placed it in a file because I don't want you to see it!
#    with open(".env") as file:
#    	apiKey = file.readline().strip()


if __name__ == "__main__":
    main(sys.argv[1:])

sys.exit(0)

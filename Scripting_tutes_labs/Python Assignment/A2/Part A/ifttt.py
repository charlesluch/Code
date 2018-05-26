#!/usr/bin/env python3

# Documentation for the requests system
# http://docs.python-requests.org/en/master/

import json
import sys
import re
import argparse
from pathlib import Path


# your program is driven by the json file, which defines what things have to happen.
# you read the file and see "ah, I have to kick off the action to get the date, then get the output from that, and feed it into the next thing to be run. I'll keep doing that until the workflow is complete, or tells me to stop."

def main(argv):

    # parses in configuration and output filenames as entered into the command line
    parser = argparse.ArgumentParser()
    output = ''
    config = ''


    if len(sys.argv) < 3:
        parser.add_argument('outputFile', help='the directory of the output file')
        args = parser.parse_args()
        output = args.outputFile
    else:
        parser.add_argument('outputFile', help='the directory of the output file')
        parser.add_argument('configFile', help='the directory of the .json configuration file')
        args = parser.parse_args()
        output = args.outputFile
        config = args.configFile

    # checkng for the existance of a .json file at the path specified
    if(config):
        p = re.compile('\S+\.json')
        re.match(p,config)
        if(match):
            jFile = Path(config)
            if jFile.is_file():
                realConfig = config
    else:
        realConfig = './ifttt.json'

        # contents of the .json file still yet to be verified


    # read the contents of the .json configuration file and let that file dictate the actions of the program.
    with open(realConfig) as c:
        plan = json.load(c)

    print(plan)


        # PROCESSING OUTPUT FILE

        # the output file is created and may not exist before the program has to run,

            #if there is output and the file is not detected, first make sure the file is created, then go on to write to it,

            #if not, then create it before you write.

    # check json for the headers as specified in the json file


	# Get the API key

	# It can be stored in the configuration file (recommended option for this program)
	# You would then read it from the command line arguments


	# I've placed it in a file because I don't want you to see it!
#    with open(".env") as file:
#    	apiKey = file.readline().strip()


if __name__ == "__main__":
    main(sys.argv[1:])

sys.exit(0)

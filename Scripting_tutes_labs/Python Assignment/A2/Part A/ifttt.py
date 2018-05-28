#!/usr/bin/env python3

# Documentation for the requests system
# http://docs.python-requests.org/en/master/

import json
import sys
import re
import argparse
import io
from pathlib import Path
from subprocess import run, PIPE
import subprocess

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
        match = re.match(p,config)
        if(match):
            jFile = Path(config)
            if jFile.is_file():
                realConfig = config
    else:
        realConfig = './ifttt.json'

    # open the .json configuration file and verify its validity
    with io.open(realConfig, 'r', encoding='utf8') as c:
        try:
            plan = json.load(c)
            c.close()
        except json.decoder.JSONDecodeError as err:
            print("\nError: there is a problem with your JSON config file:\n",err.msg,"on Line:", err.lineno, "of", str(realConfig))
            return sys.exit(1)

    # read the contents of the .json configuration file and enter program, parameters and configuration into the command line of the next subprocess

    for flow in plan['flows']:
        print("\nFlow is:", flow)
        for service in plan['flows'][flow]:

            programFile = "\"" + plan['services'][service]['program'] + "\""
            params = " ".join(plan['services'][service]['parameters'])
            cmd = programFile + params
            KVpairs = plan['services'][service]['configuration']
            for key,val in KVpairs.items():
                if(len(key) > 0):
                    flag = "--"+key
                    cmd += " " + flag + "=" + "\"" + val + "\""

            print("Service is:",plan['services'][service]['name'],"\nCommands:",cmd)

            p = run(cmd, stdout=PIPE, input='', encoding='utf-8', shell='true')

            # handle CompletedProcess
            print("Result: returncode:",p.returncode,"\tstdout:",p.stdout)

if __name__ == "__main__":
    main(sys.argv[1:])

sys.exit(0)

#!/usr/bin/env python3

import sys
import argparse

def main():

    now = sys.stdin.read()
    start = "00:00:00"
    end = "11:59:59"

    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--start",help="switches on the service's acceptance of a start time from the JSON config file via the command line  arguments of the service call",action='store',required='false',dest='start')
    parser.add_argument("-e","--end",help="switches on the service's acceptance of an end time from the JSON config file via the command line arguments of the service call",action='store',required='false',dest='end')
    args = parser.parse_args()

    if args.quiet:
        if (start <= now) and (now <= end):
            print(sys.exit(0))
        else:
            print(sys.exit(1))

    elif args.start and args.end:
        if (args.start <= now) and (now <= args.end):
            print(sys.exit(0))
        else:
            print(sys.exit(1))

    elif args.start:
        if (args.start <= now) and (now <= end):
            print(sys.exit(0))
        else:
            print(sys.exit(1))

    else:
        if (start <= now) and (now <= args.end):
            print(sys.exit(0))
        else:
            print(sys.exit(1))

try:
  main()
except:
  sys.exit(1)

sys.exit(0)

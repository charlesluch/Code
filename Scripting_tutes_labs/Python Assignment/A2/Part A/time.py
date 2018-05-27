#!/usr/bin/env python3

import datetime
import sys

def main():
    format = "%H:%M:%S"
    now = datetime.datetime.now()
    time = now.strftime(format)
    print(time)
    return sys.exit(0)

try:
    main()
except:
    sys.exit(1)

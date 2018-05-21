#!/usr/bin/env python3

import sys
import time

def main():
    start = "18:00:00"
    end = "23:59:59"
    now = time.strptime(str(time.localtime()),'%H:%M:%S')

    if(start >= now >= end):
        return sys.exit(0)
    else:
        return sys.exit(1)

try:
  main()
except:
  sys.exit(1)

sys.exit(0)

#!/usr/bin/env python3

import sys

def main():
    now = sys.stdin.read()
    print(now)
    start = "00:00:00"
    end = "11:59:59"

    if(start >= now >= end):
        sys.exit(0)
    else:
        sys.exit(1)

try:
  main()
except:
  sys.exit(1)

sys.exit(0)

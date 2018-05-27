#!/usr/bin/env python3

import sys

def main():
    now = sys.stdin.read()
    start = "12:00:00"
    end = "17:59:59"

    if(start >= now >= end):
        sys.exit(0)
    else:
        sys.exit(1)

try:
  main()
except:
  sys.exit(1)

sys.exit(0)

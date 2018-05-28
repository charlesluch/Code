#!/usr/bin/env python3

import os
import sys

def main():

# find a way to get the return code from the last process
    RC = 0

    if(RC == 1):
        return os.kill(main,SIGQUIT)
    else:
        return sys.exit(0)

main()

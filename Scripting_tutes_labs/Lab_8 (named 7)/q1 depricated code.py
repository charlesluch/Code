# 1. Write a Python function dayofyear which, given a number N, returns a string giving the Nth day of a non-leap year, in day/month format. For example, dayofyear(1) should return “January 1”, dayofyear(35) should print “February 4”, and dayofyear(365) should print “December 31”.

#! usr/bin/env python3

import sys

if len(sys.argv) > 1:
    d = sys.argv[1]
else:
    print("Error: please enter a a number between 1 and 365 to find out what day of a non-leap year it is")

# Another error to note: referring to index

for [] in array

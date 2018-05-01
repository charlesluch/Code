# 1. Write a Python function dayofyear which, given a number N, returns a string giving the Nth day of a non-leap year, in day/month format. For example, dayofyear(1) should return “January 1”, dayofyear(35) should print “February 4”, and dayofyear(365) should print “December 31”.

#! usr/bin/env python3

import sys

def dayofyear(d):

    if d > 365 or d < 1:
        print("Error: this function will not take values that assume that a year has passed and will not take numbers less than 0, please enter a number between 1 and 365")
    else:

        mDays = [31,28,31,30,31,30,31,31,30,31,30,31]
        i = 0

        for dCount in mDays:
            if d > dCount:
                d = d - dCount
                i += 1
            else:
                m = (i + 1)
                return m,d

        if m == 1:
            mStr = "January "
        elif m == 2:
            mStr = "February "
        elif m == 3:
            mStr = "March "
        elif m == 4:
            mStr = "April "
        elif m == 5:
            mStr = "May "
        elif m == 6:
            mStr = "June "
        elif m == 7:
            mStr = "July "
        elif m == 8:
            mStr = "August "
        elif m == 9:
            mStr = "September "
        elif m == 10:
            mStr = "October "
        elif m == 11:
            mStr = "November "
        elif m == 12:
            mStr = "December "
        else:
            sys.exit("Unexpected error!")

        print(mStr,d)

d = int(input('Please enter a number between 1 and 365 representing the day of the year: '))

dayofyear(d)

# 3. Try commonly used modules introduced in this week’s lecture.

#! usr/bin/env python3
import sys, os, math
from time import strftime, localtime

path = sys.argv[1]

if len(sys.argv) != 2:
    print("Error: a single file path was not detected")
    sys.exit()

elif path:
    os.open(path)
    # time
    now = strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
    os.write(path, now)
    # math
    calc = math.sqrt(time.time())
    os.write(path, calc)
    os.close(path)

# xml processing modules were omitted as python 3.6 documentation suggested that most uses of this module is unsafe.

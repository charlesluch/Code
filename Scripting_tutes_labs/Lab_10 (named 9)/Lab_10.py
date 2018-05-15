# 1. Wrtie a script that takes a command line parameter which is a URI. The URI should support the file:// and http:// prefixes. If it starts with file:// it should open the file and display it to the screen. It it starts with a http:// to treat it as a remote web page and retrieve it from the web and display the raw html to the screen. Test it on some web pages, such as http://www.cs.rmit.edu.au/.

#! usr/bin/env python3
import sys
import re
import urllib.request

# accept one command line parameter
if len(sys.argv) != 2:
    print("Error: please enter one argument")
    sys.exit()

arg = str(sys.argv[1])
pattern = re.compile(r"https://\w+"|r"http://\w+"|r"file://\w+")
m = re.match(pattern, arg)
if m:
    # if file:// prefix, open and display file contents
    file = re.compile(r"file://\w+")
    mf = re.match(file, arg)
    if mf:
        filename = arg[7]
        try:
            f = open(filename, "r")
            print(f.read())
            f.close()
        except OSError():
            print("File error detected! please check the file path")
            sys.exit()

    # if http(s):// prefix, retreive remote web page's html and display
    site = re.compile(r"https://\w+"|r"http://\w+")
    ms = re.match(site, arg)
    if ms:
        with urllib.request.urlopen(arg) as s:
            print(s.read())

else:
    print("Error: path must begin either with https://, http:// or file://")
    sys.exit()

# tested in console on http://www.cs.rmit.edu.au/



# 2. There is more than one way to handle images in the HTMLParser class. Examine the online documentation to find another method.

#! usr/bin/env python3

#

# 3. Try commonly used modules introduced in this week’s lecture.

#! usr/bin/env python3

# sys Access to aspects of the current Python runtime (command line, environment variables, standard input/output)

# os Operating system services (files, directories, processes, etc.)

# time Time/date manipulation

# math Mathematical functions (trigonometry, logarithms, etc.)

# xml Operations on XML files

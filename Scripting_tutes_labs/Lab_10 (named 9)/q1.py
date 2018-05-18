# 1. Wrtie a script that takes a command line parameter which is a URI. The URI should support the file:// and http:// prefixes. If it starts with file:// it should open the file and display it to the screen. It it starts with a http:// to treat it as a remote web page and retrieve it from the web and display the raw html to the screen. Test it on some web pages, such as http://www.cs.rmit.edu.au/.

#! usr/bin/env python3
import sys
import re
import urllib.request

# accept one command line parameter
arg = sys.argv[1]

if len(sys.argv) != 2:
    print("Error: only one argument accepted")
    sys.exit()

pattern = re.compile(r'https://.+'|r'http://.+'|r'file://.+')
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
    site = re.compile(r'https://.+'|r'http://.+')
    ms = re.match(site, arg)
    if ms:
        with urllib.request.urlopen(arg) as s:
            print(s.read())

else:
    print("Error: path must begin either with https://, http:// or file://")
    sys.exit()

# I could not figure out how to get past the syntax errors in my attempts to test this code in the console, was aiming to test on https://www.w3schools.com/

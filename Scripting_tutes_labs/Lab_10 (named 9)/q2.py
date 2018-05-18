# 2. There is more than one way to handle images in the HTMLParser class. Examine the online documentation to find another method.

#! usr/bin/env python3

# HTMLParser class handling method 1 - anchorlist (depricated)
# as referenced from the Course Material provided by RMIT in its 2018 course COSC2468: Scripting Language Programming

import sys, urllib.request
from html.parser import HTMLParser
from formatter import NullFormatter

try:
  inf = urllib.request.urlopen(sys.argv[1])
except IndexError:
  inf = sys.stdin

p = HTMLParser(NullFormatter())
p.feed(inf.read())
for link in p.anchorlist:
  print(link)

# HTMLParser class handling method 2 - the suite of handle_... methods
# obtained from https://docs.python.org/3/library/html.parser.html?highlight=handle%20html on the 17th of May, 2018
# used in this context for educational purposes only

from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = HTMLParser()
parser.feed('<html><head><title>Test</title></head>'
            '<body><h1>Parse me!</h1></body></html>')

# 1. Wrtie a script that takes a command line parameter which is a URI. The URI should support the file:// and http:// prefixes. If it starts with file:// it should open the file and display it to the screen. It it starts with a http:// to treat it as a remote web page and retrieve it from the web and display the raw html to the screen. Test it on some web pages, such as http://www.cs.rmit.edu.au/.

#! usr/bin/env python3

import urllib2

# accept command line parameter

# if file:// prefix, open and display file contents
if(input == (/$ (file://) ^/))
# if http:// prefix, retreive remote web page
elif(input == (/$ (http://) or (https://) ^/))
    url = urllib2.urlopen(input)

# test it on web pages including http://www.cs.rmit.edu.au/

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

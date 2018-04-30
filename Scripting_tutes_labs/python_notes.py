#! /usr/bin/env python3
#
#   Why python?
#   - APIs http://pypi.python.org
#   - Efficient: 1.py:3.java:10.c
#   - Powerful - treats you like an adult and so gives you agency
#   - Google and many others use it
#
#   Python3
#   - backwards incompatible
#
#   python 2: print not a function
#   print "Hello World"
#
#   python 3: print a function
print("Hello World")
#
#   ===== A note on workflow =====
#
#   I use Atom as my IDE,
#   I run the code by opening it in python IDLE and pressing F5 to run it in python shell.
#
#
#   Operators and examples

list = [0,1,2]
print(list)

list.append(list)
print(list)

listB = ['a','b','c']
list.append(listB)
print(list)

a = 1   # object 1 is set \\
b = a
del a
del b   # object 1 freed

# print(a) # ERROR: not defined

a = 2
print(a)

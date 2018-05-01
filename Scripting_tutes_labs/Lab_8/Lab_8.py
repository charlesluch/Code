#   1. Modify the stack class in the lecture notes to make a queue class. Name it “queue”.

class Queue(object):
# "A class implementing a queue data structure."
  def __init__(self):
    self.thequeue = []
  def queue(self, a):
# "Make a value enter the back of the queue thequeue[0]."
    return self.thequeue.insert(0,a)
  def leave(self):
# "Make a value leave the front of the queue."
    return self.thequeue.pop()

#   2. Create a class named “Quack”, which implements a hybrid queue/stack. It has three methods: push() which pushes something to the end, pop_end() which pops the value from the end (stack-fashion) and pop_start(), which pops from the start (queue-fashion).

class Quack(object):
  def __init__(self):
    self.thequack = []
# Push a value to the end: thequack[0]
  def push(self, a):
    self.thequeue.insert(0,a)
# Pop a value from the end: thequack[0]
  def pop_end(self):
    return self.thequack.pop(0)
# Pop a value from the start: pop operating normally
  def pop_start(self):
    return self.thequack.pop()

#   3. Modify your class from last question to include docstrings and a simple doctest for each of the methods you’ve written.

class Quack(object):
  def __init__(self):
    self.thequack = []
"""Insert the value a in the quack at index 0
>>>push('ax3')
>>>print(thequack[0])
'ax3'
"""
  def push(self, a):
    self.thequeue.insert(0,a)
"""Pop a value from the end of the quack at index 0"""
# 1 less in size and the rest of the string is the same as all but the 0th element
  def pop_end(self):
    return self.thequack.pop(0)
"""Pop a value from the start of the quack at index n"""
# 1 less in size and the rest of the string is the same as all but the nth element
  def pop_start(self):
    return self.thequack.pop()

if __name__ == "__main__":
    import doctest
    doctest.testmod()


#   4. Test sample programs in this week’s lecture

"""Module Book.

Class functions:
   books()
   booksUnder(maxPrice)
"""

__author__ = "Bingxuan Xie (bingxuan.xie@rmit.edu.au)"

# Imports.
import os

def readtable(filename):
   """Returns a list of lists of all colon-delimited lines in a file."""
   try:
      f = open(filename, "r")
      # List comprehension
      result = [line.rstrip('\n').split(':') for line in f if line.strip()]
      f.close()
      return result
   except EnvironmentError:
      return []

# Class Book.
class Book(object):
   "Class Book encalpsulates the book database."

   # Constructor.
   def __init__(self, filename):
      """The constructor. Accepts the file name and load all data from the
      file."""
      # Loads data
      self._loadBooks(filename)

   # Internal routines.
   def _loadBooks(self, filename):
      """Internal routine. Load all books from the file system."""
      # Initialisation
      self._books = {}
      # Reads subjects
      books = readtable(filename)
      # Traverses all books
      for book in books:
         # Unpacking
         bookTitle, bookPrice = book
         self._books[bookTitle] = float(bookPrice)

   # User visible interfaces.
   def books(self):
      """Returns all books in the system."""
      return self._books

   def booksUnder(self, maxPrice):
      """Returns all books under the speicified price."""

      result = {}
      for bookTitle, bookPrice in self._books.items():
         if bookPrice <= maxPrice:
            result[bookTitle] = bookPrice
      return result

# Save the module to book.py. Create a file named 'BOOKS' with the following:

Programming Python, Second Edition:59.99
Learning Python, 3rd Edition:39.99
Programming in Python 3:44.99
Learning Python, Powerful Object-Oriented Programming:54.99
Python Essential Reference (4th Edition):49.99
Now save the following script as findbook.py, use chmod +x findbook.py to make it executable.

#! /usr/bin/env python3

# Imports.
import sys, book

def showUsage():
   """Displays usage."""
   print "Usage: %s maxPrice"%sys.argv[0]

def showBooks(maxPrice):
   """Displays a list of books under the user specified price."""
   # Load books from file 'BOOKS'
   books = book.Book('BOOKS').booksUnder(maxPrice)

   # Loop through books
   for title, price in books.items():
      print "Title: %s   Price: $%.2f"%(title, price)

   # Final print
   if len(books) == 0:
      print "No match books."

# Main
argc = len(sys.argv)

if argc == 1:               # No user arguments
   showUsage()
elif argc == 2:
   program, maxPrice = sys.argv
   if maxPrice.isdigit():
      showBooks(int(maxPrice))
   else:
      showUsage()
else:
   showUsage()
Finally, run the script:

% ./findbook.py 20
No match books.
% ./findbook.py 40
Title: Learning Python, 3rd Edition   Price: $39.99
% ./findbook.py 60
Title: Python Essential Reference (4th Edition)   Price: $49.99
Title: Learning Python, 3rd Edition   Price: $39.99
Title: Programming in Python 3   Price: $44.99
Title: Learning Python, Powerful Object-Oriented Programming   Price: $54.99
Title: Programming Python, Second Edition   Price: $59.99

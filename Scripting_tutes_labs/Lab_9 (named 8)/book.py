#! /usr/bin/env python3

"""Module Book.

Class functions:
   books()
   booksUnder(maxPrice)
"""

__author__ = "Bingxuan Xie (bingxuan.xie@rmit.edu.au)"

# Imports.
import os

def readtable(filename):
"""Returns a list of lists of all colon-delimited lines in a file.

"""
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
"""The constructor. Accepts the file name and loads all data from the file.

"""
      # Loads data
      self._loadBooks(filename)

   # Internal routines.
   def _loadBooks(self, filename):
"""Internal routine. Load all books from the file system.

"""
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
"""Returns all books in the system.

"""
      return self._books

   def booksUnder(self, maxPrice):
"""Returns all books under the speicified price.

"""

      result = {}
      for bookTitle, bookPrice in self._books.items():
         if bookPrice <= maxPrice:
            result[bookTitle] = bookPrice
      return result

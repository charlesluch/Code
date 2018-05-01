# Imports.
import sys, book

def showUsage():

"""Displays usage.

"""
   print "Usage: %s maxPrice"%sys.argv[0]

def showBooks(maxPrice):

"""Displays a list of books under the user specified price.

"""
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

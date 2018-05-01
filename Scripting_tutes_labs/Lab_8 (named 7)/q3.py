# 3. The following function uses an if statement to detect a possible error condition:

# def magic(s):
#     dict = {"a":1,"e":2,"i":3,"o":4,"u":5}
#     if s in dict:
#         return dict[s]
#     else:
#         return 0

# Rewrite it to remove the if statement, and handle the error case by trapping an exception.

#! usr/bin/env python3

def magic(s):
    dict = {"a":1,"e":2,"i":3,"o":4,"u":5}
    try:
        dict[s]
        print(dict[s])
    except KeyError as e:
        print("Key Error - You entered: %s" % e)
        s = input("Please enter a, e, i, o or u: ")
        magic(s)

s = input("Enter a vowel: ")

magic(s)

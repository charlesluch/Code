#   3. Modify your class from last question to include docstrings and a simple doctest for each of the methods you’ve written.

#! /usr/bin/env python3
class Quack(object):
  def __init__(self):
    self.thequack = []
  def push(self, a):
    self.thequack.insert(0,a)
"""Insert the value a in the quack at index 0
>>>push('ax3')
>>>print(thequack[0])
'ax3'
"""

# 1 less in size and the rest of the string is the same as all but the 0th element
  def pop_end(self):
    return self.thequack.pop(0)
"""Pop a value from the end of the quack at index 0

>>>a=len(self.thequack)
>>>b="Inserted Value"
>>>c=thequack
>>>pop_end(b)
>>>d=len(self.thequack)
>>>e=thequack
>>>e.insert(0,b) == c
True
>>>a == (d + 1)
True

"""

# 1 less in size and the rest of the string is the same as all but the nth element
  def pop_start(self):
    return self.thequack.pop()
"""Pop a value from the start of the quack at index n

>>>a=len(self.thequack)
>>>b="Inserted Value"
>>>c=thequack
>>>pop_start(b)
>>>d=len(self.thequack)
>>>e=thequack
>>>e.insert(d,b) == c
True
>>>a == (d + 1)
True

"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()

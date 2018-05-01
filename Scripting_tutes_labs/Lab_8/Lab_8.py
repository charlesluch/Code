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
"""Push a value to the end of the quack at index 0"""
  def push(self, a):
    self.thequeue.insert(0,a)
"""Pop a value from the end of the quack at index 0"""
  def pop_end(self):
    return self.thequack.pop(0)
"""Pop a value from the start of the quack at index n"""
  def pop_start(self):
    return self.thequack.pop()

if __name__ == "__main__":
    import doctest
    doctest.testmod()


#   4. Test sample programs in this week’s lecture

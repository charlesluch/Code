#   2. Create a class named “Quack”, which implements a hybrid queue/stack. It has three methods: push() which pushes something to the end, pop_end() which pops the value from the end (stack-fashion) and pop_start(), which pops from the start (queue-fashion).

#! /usr/bin/env python3
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

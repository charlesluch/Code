#   1. Modify the stack class in the lecture notes to make a queue class. Name it “queue”.

#! /usr/bin/env python3
class Queue(object):
# "A class implementing a queue data structure."
  def __init__(self):
    self.thequeue = []
  def queue(self, a):
# "Make a value enter the back of the queue thequeue[0]."
    self.thequeue.insert(0,a)
  def leave(self):
# "Make a value leave the front of the queue."
    return self.thequeue.pop()

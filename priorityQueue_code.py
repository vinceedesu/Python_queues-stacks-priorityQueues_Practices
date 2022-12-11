#source: https://realpython.com/queue-in-python/#learning-about-the-types-of-queues

from collections import deque
from heapq import heappop, heappush

# Handling Corner Cases in Your Priority Queue import
from itertools import count

class PriorityQueue:
    # array for init self
    def __init__(self):
        self._elements =[]
        self._counter = count()
        
    # heapush - This function adds an element to the heap without altering the current heap.
    def enqueue_with_priority(self, priority, value):
        # least to most  1 2 3
        # heappush(self._elements, (priority,value))

        # reserve make the priority negative most to least 3 2 1
        # heappush(self._elements,(-priority,value))
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)
        
    # heappop - This function is used to remove and return the smallest element from the heap
    def dequeue(self):
        # return heappop(self._elements)
        # return heappop(self._elements)[1]
        return heappop(self._elements)[-1]
    
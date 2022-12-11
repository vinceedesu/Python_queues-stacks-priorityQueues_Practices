from collections import deque
from heapq import heappop, heappush

class PriorityQueue:
    # array for init self
    def __init__(self):
        self._elements =[]
        
    # heapush - This function adds an element to the heap without altering the current heap.
    def enqueue_with_priority(self, priority, value):
        # least to most  1 2 3
        # heappush(self._elements, (priority,value))

        # reserve make the priority negative most to least 3 2 1
        heappush(self._elements(-priority,value))
    # heappop - This function is used to remove and return the smallest element from the heap
    def dequeue(self):
        # return heappop(self._elements)
        return heappop(self._elements)[1]
    
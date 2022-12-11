from collections import deque
from heapq import heappop, heappush

class PriorityQueue:
    # array for init self
    def __init__(self):
        self._elements =[]
        
    def enqueue_with_priority(self, priority, value):
        heappush(self._elements, (priority,value))
    
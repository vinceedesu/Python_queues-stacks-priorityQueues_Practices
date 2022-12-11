# stack_code.py
#source: https://realpython.com/queue-in-python/#learning-about-the-types-of-queues
#just copy queue_code, priorityQueue_code and stack_code and make IterankeMixin class as parent class

from collections import deque
from heapq import heappop, heappush
from itertools import count

class IterableMixin:
    def __len__(self):
        return len(self._elements)
    
    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

class Queue(IterableMixin):
    def __init__(self, *elements):
        self._elements = deque(elements)
    
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()

    def enqueue(self, element):
        self._elements.append(element)
    
    def dequeue(self):
        return self._elements.popleft()

# stack class

# calling-out Queue class fron queue_code
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()

# just copy the same Priority Q with IterableMixin 
class PriorityQueue(IterableMixin):
        # array for init self
    def __init__(self):
        self._elements =[]
        # adding a counter
        self._counter = count()
        
    # heapush - This function adds an element to the heap without altering the current heap.
    def enqueue_with_priority(self, priority, value):
        element = (-priority, next(self._counter), value)
        heappush(self._elements, element)
        
    # heappop - This function is used to remove and return the smallest element from the heap
    def dequeue(self):
        return heappop(self._elements)[-1]
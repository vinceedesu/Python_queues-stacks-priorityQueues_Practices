# Queue: First-In, First-Out (FIFO)
# queues.py

from collections import deque

class Queue:
    
    # NEW TERM  __init___
    # The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach
    # The __init__ function is called every time an object is created from a class.
    
    # def __init__(self):
    #     self._elements = deque()

    # deque() is a double-ended queue in which elements can be both inserted and deleted from either the left or the right end of the queue. 
    # Dequeue: Remove an element from the front of the queue.     
    # Enqueue: Add an element to the end of the queue. 

    # def enqueue(self, element):
    #     self._elements.append(element)
    
    # # popleft() removes an element from the left side of the deque and returns the value.   
    # def dequeue(self):
    #     return self._elements.popleft()
    
    
# As expected, the enqueued elements come back to you in their original order. 
# If you want, you may improve your class by making it iterable and able to report its length and optionally accept initial elements:

    def __init__(self, *elements):
        self._elements = deque(elements)
        
     
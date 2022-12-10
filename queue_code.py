# Queue: First-In, First-Out (FIFO)
# queues.py

from collections import deque

class Queue:
    
    # NEW TERM  __init___
    # The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach
    # The __init__ function is called every time an object is created from a class.
    
    def __init__(self):
        self._elements = deque()

    # deque() is a double-ended queue in which elements can be both inserted and deleted from either the left or the right end of the queue. 
    # Dequeue: Remove an element from the front of the queue.     
    # Enqueue: Add an element to the end of the queue. 

    def enqueue(self, element):
        self._elements.append(element)
        
    
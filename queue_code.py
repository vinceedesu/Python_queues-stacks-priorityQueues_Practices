# Queue: First-In, First-Out (FIFO)
# queues.py

from collections import deque

class Queue:
    
    # NEW TERM  __init___
    # The __init__ method is the Python equivalent of the C++ constructor in an object-oriented approach
    # The __init__ function is called every time an object is created from a class.
    
    def __init__(self):
        self._elements = deque()


# stack_code.py
#source: https://realpython.com/queue-in-python/#learning-about-the-types-of-queues
#just copy queue_code

from queue_code import Queue
from collections import deque

# class Queue:
#     def __init__(self, *elements):
#         self._elements = deque(elements)
    
#     def __len__(self):
#         return len(self._elements)

#     def __iter__(self):
#         while len(self) > 0:
#             yield self.dequeue()

#     def enqueue(self, element):
#         self._elements.append(element)
    
#     def dequeue(self):
#         return self._elements.popleft()

# stack class

# calling-out Queue class fron queue_code
class Stack(Queue):
    def dequeue(self):
        return self._elements.pop()
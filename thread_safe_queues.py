# thread_safe_queues.py
import argparse
#queue is a library for queues and the likes
from queue import LifoQueue, PriorityQueue, Queue

QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}

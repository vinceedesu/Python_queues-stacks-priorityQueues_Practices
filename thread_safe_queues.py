# thread_safe_queues.py
import argparse
#queue is a library for queues and the likes
from queue import LifoQueue, PriorityQueue, Queue

#dictionary for queues
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}


def main(args):
    buffer = QUEUE_TYPES[args.queue]()
    
def parse_args():
    parser = argparse.ArgumentParser()
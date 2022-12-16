# thread_safe_queues.py
import argparse
#queue is a library for queues and the likes
from queue import LifoQueue, PriorityQueue, Queue

#added threading
import threading

#dictionary for queues
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}


def main(args):
    buffer = QUEUE_TYPES[args.queue]()
    
def parse_args():
    #The argparse module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid argumentsThe argparse module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--queue", choices=QUEUE_TYPES, default="fifo")
    parser.add_argument("-p", "--producers", type=int, default=3)
    parser.add_argument("-c", "--consumers", type=int, default=2)
    parser.add_argument("-ps", "--producer-speed", type=int, default=1)
    parser.add_argument("-cs", "--consumer-speed", type=int, default=1)
    return parser.parse_args()

#dont know what this does... 
if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        pass


#added products
PRODUCTS = (
    ":balloon:",
    ":cookie:",
    ":crystal_ball:",
    ":diving_mask:",
    ":flashlight:",
    ":gem:",
    ":gift:",
    ":kite:",
    ":party_popper:",
    ":postal_horn:",
    ":ribbon:",
    ":rocket:",
    ":teddy_bear:",
    ":thread:",
    ":yo-yo:",
)


#added class worker 
class Worker(threading.Thread):
    def __init__(self,speed, buffer):
        super().__init__(daemon=True)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0

    
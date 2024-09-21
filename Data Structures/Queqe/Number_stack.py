# Importing the module
from collections import deque

# Queue class
class Queue:
    def __init__(self):
        self.buffer = deque()

    # To add element at begining
    def enqueue(self, val):
        self.buffer.appendleft(val)

    # To remove element at end
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    
    # To find the the queue is empty or not
    def is_empty(self):
        return len(self.buffer) == 0

    # To find the size of queue
    def size(self):
        return len(self.buffer)

    # To find peak of the queue
    def front(self):
        return self.buffer[-1]

def produce_binary_numbers(n):
    numbers_queue = Queue()
    numbers_queue.enqueue("1")

    for i in range(n):
        front = numbers_queue.front()
        print("   ", front)
        numbers_queue.enqueue(front + "0")
        numbers_queue.enqueue(front + "1")

        numbers_queue.dequeue()


if __name__ == '__main__':
    produce_binary_numbers(10)
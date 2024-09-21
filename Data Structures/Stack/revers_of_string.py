# Import the module
from collections import deque


# Stack class
class Stack:
    def __init__(self):
        self.container = deque()

    # To Add the elements at the end of the stack
    def push(self, val):
        self.container.append(val)

    # To Remove the elements at the end of the stack
    def pop(self):
        return self.container.pop()

    # To find the peek of the stack
    def peek(self):
        return self.container[-1]

    # To find the stack is empty or not
    def is_empty(self):
        return len(self.container) == 0

    # To find the size of the stack
    def size(self):
        return len(self.container)

# reversing the string using stack data structure
def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("Good Day"))
    print(reverse_string("I am the king"))
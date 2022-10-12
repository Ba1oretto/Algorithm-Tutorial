import unittest
from gradescope_utils.autograder_utils.decorators import weight
from adts import *
from utils import *

class TestStacksQueues(unittest.TestCase):

    @weight(0.5)
    def test_1(self):
        """04 ADTs: Push and peek with dynamic array."""
        stack = StackOrQueue()
        stack.push('A')
        stack.push('B')
        self.assertEqual(stack.peek(),'B')

    @weight(0.5)
    def test_2(self):
        """04 ADTs: Push and peek with linked list."""
        stack = StackOrQueue(useLinkedList=True)
        stack.push('A')
        stack.push('B')
        self.assertEqual(type(stack.peek()),Node)
        self.assertEqual(stack.peek().data,'B')

    @weight(0.5)
    def test_3(self):
        """04 ADTs: Enqueue and peek with dynamic array."""
        queue = StackOrQueue(isQueue=True)
        queue.push('A')
        queue.push('B')
        self.assertEqual(queue.peek(),'A')

    @weight(0.5)
    def test_4(self):
        """04 ADTs: Enqueue and peek with dynamic array."""
        queue = StackOrQueue(isQueue=True, useLinkedList=True)
        queue.push('A')
        queue.push('B')
        self.assertEqual(type(queue.peek()), Node)
        self.assertEqual(queue.peek().data,'A')

    @weight(0.5)
    def test_5(self):
        """04 ADTs: Push and pop with dynamic array."""
        stack = StackOrQueue()
        stack.push('A')
        stack.push('B')
        self.assertEqual(stack.pop(),'B')
        self.assertEqual(stack.peek(),'A')

    @weight(1)
    def test_6(self):
        """04 ADTs: Push and peek with linked list."""
        stack = StackOrQueue(useLinkedList=True)
        stack.push('A')
        stack.push('B')
        self.assertEqual(type(stack.peek()),Node)
        self.assertEqual(stack.pop().data,'B')
        self.assertEqual(stack.peek().data,'A')

    @weight(0.5)
    def test_7(self):
        """04 ADTs: Enqueue and peek with dynamic array."""
        queue = StackOrQueue(isQueue=True)
        queue.push('A')
        queue.push('B')
        self.assertEqual(queue.pop(),'A')
        self.assertEqual(queue.peek(),'B')        

    @weight(1)
    def test_8(self):
        """04 ADTs: Enqueue and peek with dynamic array."""
        queue = StackOrQueue(isQueue=True, useLinkedList=True)
        queue.push('A')
        queue.push('B')
        self.assertEqual(type(queue.peek()), Node)
        self.assertEqual(queue.pop().data,'A')
        self.assertEqual(queue.peek().data,'B')  


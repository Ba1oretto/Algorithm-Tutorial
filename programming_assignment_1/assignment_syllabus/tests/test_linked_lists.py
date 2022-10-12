import unittest
from gradescope_utils.autograder_utils.decorators import weight
from linkedlist import LinkedList
from utils import *

class TestLinkedList(unittest.TestCase):
    @weight(0.25)
    def test1(self):
        """03 Linked List: Checking length and size of LinkedList."""
        arr = LinkedList()
        arr[0] = '0'
        for i in range(1,10):
            arr[i] = i
            self.assertEqual(type(arr[i]), Node)
            self.assertEqual(len(arr),i+1)
            self.assertEqual(arr.get_size(),i+1)
            
    @weight(0.25)
    def test2(self):
        """03 Linked List: Shifting property when adding new values."""
        arr = LinkedList()
        for i in range(5):
            arr[0] = i
            self.assertEqual(type(arr[i]), Node)
            self.assertEqual(arr[i].next,None)
        for i in range(5):
            self.assertEqual(type(arr[i]), Node)
            self.assertEqual(arr[i].data,4-i)

        arr = LinkedList()
        for i in range(5):
            arr[1] = i
            self.assertEqual(type(arr[i]), Node)
            self.assertEqual(arr[i].next,None)
        for i, v in enumerate([0,4,3,2,1]):
            self.assertEqual(type(arr[i]), Node)
            self.assertEqual(arr[i].data, v)

    @weight(0.25)
    def test3(self):
        """03 Linked List: Shifting property when removing values."""
        arr = LinkedList()
        for i in range(5):
            arr[0] = i
        for i in range(4):
            del arr[0]
            self.assertEqual(type(arr[0]), Node)
            self.assertEqual(arr[0].data,3-i)

        arr = LinkedList()
        for i in range(5):
            arr[0] = i
        for i in range(3):
            del arr[1]
            self.assertEqual(type(arr[1]), Node)
            self.assertEqual(arr[1].data,2-i)

    @weight(0.25)
    def test4(self):
        """03 Linked List: Doubly property."""
        arr = LinkedList(isDoubly=True)
        for i in range(10):
            arr[0] = i
            self.assertEqual(len(arr),i+1)
        for i in range(9):
            self.assertEqual(arr[i+1].prev, arr[i])

    @weight(0.5)
    def test5(self):
        """03 Linked List: Basic traversing."""
        arr = LinkedList()
        for i in range(10):
            arr.append(i)
            self.assertEqual(len(arr),i+1)
        for i in range(9):
            self.assertEqual(arr[i].next, arr[i+1])

    @weight(0.5)
    def test6(self):
        """03 Linked List: Extend with static array."""
        arr = LinkedList()
        arr.append(1)
        anotherArray = StaticArray(10)
        for i in range(10):
            anotherArray.append(i)
        arr.extend(anotherArray)
        for i,v in enumerate([1]+list(range(10))):
            self.assertEqual(type(arr[i]),Node)
            self.assertEqual(arr[i].data,v)

    @weight(0.5)
    def test7(self):
        """03 Linked List: Iterable check"""
        arr = LinkedList()
        for i in range(10):
            arr.append(i)
        for i,n in enumerate(arr):
            self.assertEqual(type(n),Node)
            self.assertEqual(n.data,i)


    @weight(0.5)
    def test8(self):
        """03 Linked List: Removing values and checking argwhere."""
        arr = LinkedList()
        for i in range(10):
            arr.append(i)
            arr.append(i)
            ans = StaticArray(2)
            ans.append(2*i)
            ans.append(2*i+1)
            self.assertEqual(arr.argwhere(i),ans)
        for i in range(10):
            arr.remove(i)
            ans = StaticArray(1)
            ans.append(i)
            self.assertEqual(arr.argwhere(i),ans)

    @weight(0.5)
    def test9(self):
        """03 Linked List: Checking whether equals is working."""
        arr1 = LinkedList()
        arr2 = LinkedList()
        for i in range(10):
            arr1.append(i)
            arr2.append(i)
            self.assertEqual(arr1,arr2)

        arr1 = LinkedList()
        arr2 = LinkedList()
        for i in range(10):
            arr1.append(i)
            arr2.append(9-i)
        self.assertNotEqual(arr1,arr2)

        arr1 = LinkedList()
        arr2 = LinkedList()
        for i in range(10):
            arr1.append(i)
            arr2.append(i)
        del arr2[0]
        self.assertNotEqual(arr1,arr2)

    @weight(0.5)
    def test10(self):
        """03 Linked List: Checking circular property."""
        arr = LinkedList(isCircular=True)
        for i in range(10):
            arr.append(i)
        j = 0
        for n in arr:
            self.assertEqual(n.data, (j+10)%10)
            j+=1
            if j==20:
                break

    @weight(1)
    def test11(self):
        """03 Linked List: Checking circular doubly property."""
        arr = LinkedList(isCircular=True, isDoubly=True)
        for i in range(10):
            arr.append(i)
        j = 0
        for n in arr:
            self.assertEqual(n.data, (j+10)%10)
            self.assertEqual(n.prev.data, (j+10-1)%10)
            j += 1
            if j==20:
                break

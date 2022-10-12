import unittest
from gradescope_utils.autograder_utils.decorators import weight
from arrays import DynamicArray
from utils import *

class TestDynamicArray(unittest.TestCase):
    @weight(0.25)
    def test1(self):
        """02 Dynamic Array: Checking length and size of empty DynamicArray."""
        for i in range(1,10):
            arr = DynamicArray(i)
            self.assertEqual(len(arr),0)
            self.assertEqual(arr.get_size(),i)
            
    @weight(0.25)
    def test2(self):
        """02 Dynamic Array: Shifting property when adding new values."""
        arr = DynamicArray(10)
        for i in range(5):
            arr[0] = i
            self.assertEqual(len(arr),i+1)
            self.assertEqual(arr.get_size(),10)
        for i in range(5):
            self.assertEqual(arr[i],4-i)
            self.assertEqual(arr.get_size(),10)

    @weight(0.25)
    def test3(self):
        """02 Dynamic Array: Shifting property when removing values."""
        arr = DynamicArray(10)
        for i in range(7):
            arr[0] = i
            self.assertEqual(len(arr),i+1)
            self.assertEqual(arr.get_size(),10)
        for i in range(4):
            del arr[0]
            self.assertEqual(arr[0],5-i)
            self.assertEqual(len(arr),6-i)
            self.assertEqual(arr.get_size(),10)

        arr = DynamicArray(10)
        for i in range(7):
            arr[0] = i
            self.assertEqual(len(arr),i+1)
            self.assertEqual(arr.get_size(),10)
        for i in range(3):
            del arr[1]
            self.assertEqual(arr[1],4-i)
            self.assertEqual(len(arr),6-i)
            self.assertEqual(arr.get_size(),10)

    @weight(0.25)
    def test4(self):
        """02 Dynamic Array: Resizing property when adding new values."""
        arr = DynamicArray(10)
        for i in range(10):
            arr[0] = i
            self.assertEqual(len(arr),i+1)
            if i<8:
                self.assertEqual(arr.get_size(),10)
            else:
                self.assertEqual(arr.get_size(),20)

    @weight(0.5)
    def test5(self):
        """02 Dynamic Array: Resizing property when appending new values."""
        arr = DynamicArray(10)
        for i in range(10):
            arr.append(i)
            self.assertEqual(len(arr),i+1)
            if i<8:
                self.assertEqual(arr.get_size(),10)
            else:
                self.assertEqual(arr.get_size(),20)

    @weight(0.5)
    def test6(self):
        """02 Dynamic Array: Resizing property when extending another array. Also checks extend is working properly."""
        arr = DynamicArray(10)
        arr.append(1)
        anotherArray = StaticArray(10)
        for i in range(10):
            anotherArray.append(i)
        arr.extend(anotherArray)

        for i,v in enumerate([1]+list(range(10))):
            self.assertEqual(arr[i],v)
        self.assertEqual(len(arr),11)
        self.assertEqual(arr.get_size(),20)

    @weight(0.5)
    def test7(self):
        """02 Dynamic Array: Resizing property when deleting value"""
        arr = DynamicArray(10)
        for i in range(7):
            arr.append(i)
        for i in range(7):
            del arr[0]
            if i < 5:
                self.assertEqual(10, arr.get_size())
            elif i == 5:
                self.assertEqual(5, arr.get_size())
            else:
                self.assertEqual(2, arr.get_size())

    @weight(0.5)
    def test8(self):
        """02 Dynamic Array: Resizing property when removing value"""
        arr = DynamicArray(10)
        for i in range(7):
            arr.append(i)
        for i in range(7):
            arr.remove(i)
            if i < 5:
                self.assertEqual(10, arr.get_size())
            elif i == 5:
                self.assertEqual(5, arr.get_size())
            else:
                self.assertEqual(2, arr.get_size())


    @weight(0.5)
    def test9(self):
        """02 Dynamic Array: Removing values and checking argwhere."""
        arr = DynamicArray(10)
        for i in range(7):
            arr.append(i)
            arr.append(i)
            ans = StaticArray(2)
            ans.append(2*i)
            ans.append(2*i+1)
            self.assertEqual(arr.argwhere(i),ans)
        for i in range(7):
            arr.remove(i)
            ans = StaticArray(1)
            ans.append(i)
            self.assertEqual(arr.argwhere(i),ans)

    @weight(0.5)
    def test10(self):
        """02 Dynamic Array: Checking whether equals is working."""
        arr1 = DynamicArray(10)
        arr2 = DynamicArray(10)
        for i in range(10):
            arr1.append(i)
            arr2.append(i)
            self.assertEqual(arr1,arr2)

        arr1 = DynamicArray(10)
        arr2 = DynamicArray(10)
        for i in range(10):
            arr1.append(i)
            arr2.append(9-i)
        self.assertNotEqual(arr1,arr2)

        arr1 = DynamicArray(10)
        arr2 = DynamicArray(5)
        for i in range(10):
            arr1.append(i)
            arr2.append(i)
            self.assertEqual(arr1,arr2)

        arr1 = DynamicArray(10)
        arr2 = DynamicArray(5)
        for i in range(10):
            arr1.append(i)
            arr2.append(i)
        del arr1[0]
        self.assertNotEqual(arr1,arr2)

    @weight(1)
    def test11(self):
        """02 Dynamic Array: Enforcing set property."""
        arr = DynamicArray(10, isSet=True)
        for i in range(10):
            arr[0] = i 
            arr[0] = i 
            self.assertEqual(len(arr), i+1)

        arr = DynamicArray(10, isSet=True)
        for i in range(10):
            arr[0] = i
            arr.append(i)
            self.assertEqual(len(arr), i+1)
            self.assertEqual(arr[0], i)

        arr = DynamicArray(10, isSet=True)
        for i in range(10):
            arr.append(i)
            arr[0] = i
            self.assertEqual(len(arr), i+1)
            self.assertEqual(arr[i], i)

        arr = DynamicArray(10, isSet=True)
        for i in range(10):
            arr.extend([i,i,i,i,i,i])
            self.assertEqual(len(arr), i+1)
            self.assertEqual(arr[i], i)
import unittest
from gradescope_utils.autograder_utils.decorators import weight
from pythonreview import *

class TestPythonReview(unittest.TestCase):
    @weight(0.5)
    def test_case1(self):
        """01 Python Review: Empty array should always return an empty dict"""
        arr = []
        for value in range(10):
            output = findWithSum(arr,value)
            self.assertIsInstance(output, dict)
            self.assertEqual(output, {})

    @weight(0.5)
    def test_case2(self):
        """01 Python Review: n = 0 should always return an empty dict"""
        n = 0
        for value in range(10):
            arr = list(range(value+1))
            output = findWithSum(arr,value,n)
            self.assertIsInstance(output, dict)
            self.assertEqual(output, {})

    @weight(0.5)
    def test_case3(self):
        """01 Python Review: Test with invalid inputs"""

        arr = [1,2,3]
        value = 4
        n = 3
        output = findWithSum(arr,value,n)
        self.assertIsInstance(output, dict)
        self.assertEqual(output,{})

        arr = [1,2,3]
        value = 1
        n = 2
        output = findWithSum(arr,value,n)
        self.assertIsInstance(output, dict)
        self.assertEqual(output,{})

        arr = [1,2,3]
        value = 3
        n = 3
        output = findWithSum(arr,value,n)
        self.assertIsInstance(output, dict)
        self.assertEqual(output,{})

    @weight(0.5)
    def test_case4(self):
        """01 Python Review: Check whether sum is correct"""
        arr = [1,2,3]
        value = 3
        n = 2
        output = findWithSum(arr,value,n)
        self.assertIsInstance(output, dict)
        self.assertEqual(sum(output.values()),value)

    @weight(0.5)
    def test_case5(self):
        """01 Python Review: Check whether indexing is correct"""
        arr = [1,2,3]
        value = 3
        n = 2
        output = findWithSum(arr,value,n)
        self.assertIsInstance(output, dict)
        for k,v in output.items():
            self.assertEqual(arr[k],v)

    @weight(0.5)
    def test_case6(self):
        """01 Python Review: Two more test cases"""
        arr = [10,10,20]
        value = 20
        n = 1
        output = findWithSum(arr,value,n)
        self.assertIsInstance(output, dict)
        self.assertEqual(output,{2:20})

        n = 2
        output = findWithSum(arr,value,n)
        self.assertIsInstance(output, dict)
        self.assertEqual(output,{0:10,1:10})




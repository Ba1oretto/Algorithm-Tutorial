import unittest
from gradescope_utils.autograder_utils.decorators import weight
from recursion import *

class TestRecursion(unittest.TestCase):
    @weight(0.5)
    def test_case1(self):
        """01 Recursion: n = m = 0"""
        output = howManyGroups(0, 0)
        self.assertEqual(output, 1)
    @weight(0.5)
    def test_case2(self):
        """01 Recursion: n > 0, m = 0"""
        for n in range(1,10):
            answer = 0
            output = howManyGroups(n, 0)
            self.assertEqual(output, 0)
    @weight(0.5)
    def test_case3(self):
        """01 Recursion: m = 1"""
        for n in range(10):
            output = howManyGroups(n, 1)
            self.assertEqual(output, 1)
    @weight(1.75)
    def test_case4(self):
        """01 Recursion: n = 8, m <= 8"""
        answer = [0,1,5,10,15,18,20,21]
        for m in range(8):
            output = howManyGroups(8, m)
            self.assertEqual(output, answer[m])
    @weight(1.75)
    def test_case5(self):
        """01 Recursion: n <= 8, m = 8"""
        answer = [1,1,2,3,5,7,11,15]
        for n in range(8):
            output = howManyGroups(n, 8)
            self.assertEqual(output, answer[n])
    
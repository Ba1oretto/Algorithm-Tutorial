import unittest
from gradescope_utils.autograder_utils.decorators import weight
from graph import *
from dijkstras import *

class TestDijkstras(unittest.TestCase):
    @weight(2)
    def test_case1(self):
        """04 Dijkstras: See graph1.png"""
        g = Graph()
        for v in ['a','b','c','d','e','f','g']:
            g.addVertex(v)
        g.addUndirectedEdge('a','b',7)
        g.addUndirectedEdge('a','d',5)

        g.addUndirectedEdge('b','c',8)
        g.addUndirectedEdge('b','d',9)
        g.addUndirectedEdge('b','e',7)

        g.addUndirectedEdge('c','e',5)

        g.addUndirectedEdge('d','e',15)
        g.addUndirectedEdge('d','f',6)

        g.addUndirectedEdge('e','f',8)
        g.addUndirectedEdge('e','g',9)

        g.addUndirectedEdge('f','g',11)

        answer = {'a': {'a': 0, 'b': 7, 'c': 15, 'd': 5, 'e': 14, 'f': 11, 'g': 22},
                 'b': {'a': 7, 'b': 0, 'c': 8, 'd': 9, 'e': 7, 'f': 15, 'g': 16},
                 'c': {'a': 15, 'b': 8, 'c': 0, 'd': 17, 'e': 5, 'f': 13, 'g': 14},
                 'd': {'a': 5, 'b': 9, 'c': 17, 'd': 0, 'e': 14, 'f': 6, 'g': 17},
                 'e': {'a': 14, 'b': 7, 'c': 5, 'd': 14, 'e': 0, 'f': 8, 'g': 9},
                 'f': {'a': 11, 'b': 15, 'c': 13, 'd': 6, 'e': 8, 'f': 0, 'g': 11},
                 'g': {'a': 23, 'b': 16, 'c': 14, 'd': 17, 'e': 9, 'f': 11, 'g': 0}}
        for k,c in answer.items():
            out = dijkstras(g,k)
            for v, cost in c.items():
                self.assertEqual(out[v],cost)

    @weight(2)
    def test_case3(self):
        """04 Dijkstras: runDijkstras Test"""
        out = runDijkstras()
        cities = ['Wisconsin, USA', 'West Virginia, USA', 'Vermont, USA', 'Texas, USA', 'South Dakota, US', 'Rhode Island, US','Oregon, US', 'New York, USA', 'New Hampshire, USA', 'Nebraska, USA']
        for v, min_, max_ in zip(cities,
                                [147, 147, 164, 205, 177, 171, 327, 154, 172, 174],
                                [148, 148, 165, 206, 178, 172, 328, 155, 173, 175]):
            s = sum(out[v].values())
            self.assertTrue(s>min_)
            self.assertTrue(s<max_)
            for c in cities:
                self.assertTrue(c in out.keys())
            
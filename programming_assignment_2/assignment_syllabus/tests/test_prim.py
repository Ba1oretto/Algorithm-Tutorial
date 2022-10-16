import unittest
from gradescope_utils.autograder_utils.decorators import weight
from graph import *
from prims import *

class TestPrim(unittest.TestCase):
    @weight(2)
    def test_case1(self):
        """03 Prims: See graph1.png"""
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

        out = prim(g)

        answer = [['a', 'd', 5],
                 ['d', 'f', 6],
                 ['a', 'b', 7],
                 ['b', 'e', 7],
                 ['e', 'c', 5],
                 ['e', 'g', 9]]
        for e in answer:
            self.assertTrue(e in out)
        self.assertEqual(len(answer),len(out))

    @weight(2)
    def test_case3(self):
        """03 Prims: runPrims Test"""
        out = runPrim()
        cities = ['Wisconsin, USA', 'West Virginia, USA', 'Vermont, USA', 'Texas, USA', 'South Dakota, US', 'Rhode Island, US','Oregon, US', 'New York, USA', 'New Hampshire, USA', 'Nebraska, USA']                     
        self.assertEqual(len(out),9)
        self.assertTrue(sum([i[-1] for i in out])<68)
        cs = []
        for i in out:
            cs.extend(i[:2])
        self.assertEqual(set(cities),set(cs))



        
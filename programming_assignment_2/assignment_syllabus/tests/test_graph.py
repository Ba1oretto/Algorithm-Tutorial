import unittest
from gradescope_utils.autograder_utils.decorators import weight
from graph import *

class TestGraphs(unittest.TestCase):
    @weight(0.1)
    def test_case1(self):
        """02 Graph: Checking empty graphs."""
        g = Graph()
        self.assertEqual(g.V(),[])
        self.assertEqual(g.E(),[])

    @weight(0.3)
    def test_case2(self):
        """02 Graph: Adding new vertices and checking all vertices"""
        g = Graph()
        g.addVertex('a')
        g.addVertex('b')
        g.addVertex('c')
        for i in ['a','b','c']:
            self.assertTrue(i in g.V())
        self.assertEqual(len(g.V()),3)

    @weight(0.3)
    def test_case3(self):
        """02 Graph: Removing vertices"""
        g = Graph()
        g.addVertex('a')
        g.addVertex('b')
        g.addVertex('c')
        g.removeVertex('a')
        for i in ['b','c']:
            self.assertTrue(i in g.V())
        self.assertEqual(len(g.V()),2)

    @weight(0.3)
    def test_case4(self):
        """02 Graph: Adding weighted directed edges"""
        g = Graph()
        g.addVertex('a')
        g.addVertex('b')
        g.addVertex('c')
        g.addEdge('a','b',10)
        g.addEdge('b','c',20)
        for i in [['a', 'b', 10], ['b', 'c', 20]]:
            self.assertTrue(i in g.E())

    @weight(0.25)
    def test_case5(self):
        """02 Graph: Removing weighted directed edges"""
        g = Graph()
        g.addVertex('a')
        g.addVertex('b')
        g.addVertex('c')
        g.addEdge('a','b',10)
        g.addEdge('b','c',20)
        g.removeEdge('a','b')
        self.assertTrue(['b', 'c', 20] in g.E())
        self.assertFalse(['a', 'b', 10] in g.E())
        self.assertEqual(len(g.E()),1)

    @weight(0.5)
    def test_case6(self):
        """02 Graph: Removing connected vertex"""
        g = Graph()
        g.addVertex('a')
        g.addVertex('b')
        g.addVertex('c')
        g.addUndirectedEdge('a','b',10)
        g.addUndirectedEdge('a','c',30)
        g.addEdge('b','c',20)
        self.assertEqual(len(g.V()),3)
        self.assertEqual(len(g.E()),5)
        g.removeVertex('a')
        self.assertEqual(len(g.V()),2)
        self.assertEqual(len(g.E()),1)

    @weight(0.25)
    def test_case7(self):
        """02 Graph: Neighbors of vertices"""
        g = Graph()
        g.addVertex('a')
        g.addVertex('b')
        g.addVertex('c')
        g.addUndirectedEdge('a','b',10)
        g.addUndirectedEdge('a','c',30)
        g.addEdge('b','c',20)

        out = [i for i in g.neighbors('a')]
        self.assertEqual(len(out),2)
        for i in ['b','c']:
            self.assertTrue(i in out)
        out = [i for i in g.neighbors('b')]
        self.assertEqual(len(out),2)
        for i in ['a','c']:
            self.assertTrue(i in out)
        out = [i for i in g.neighbors('c')]
        self.assertEqual(len(out),1)
        for i in ['a']:
            self.assertTrue(i in out)

    @weight(1)
    def test_case8(self):
        """02 Graph: DFT 1"""
        answer = [[0, 1, 3, 2],
                  [1, 0, 2, 3],
                  [2, 0, 1, 3],
                  [3]]
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addUndirectedEdge(0,1,10)
        g.addEdge(1,3,10)
        g.addUndirectedEdge(0,2,30)
        for i,ans in enumerate(answer):
            self.assertEqual(g.dft(i),ans)

    @weight(1)
    def test_case9(self):
        """02 Graph: DFT 2"""
        answer = [[0, 1, 2, 4, 5, 3],
                  [1, 0, 2, 4, 3, 5],
                  [2, 0, 1, 5, 3, 4],
                  [3, 0, 1, 2, 4, 5],
                  [4, 2, 0, 1, 5, 3],
                  [5],
                  [6],
                  [7, 6]]
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addVertex(4)
        g.addVertex(5)
        g.addVertex(6)
        g.addVertex(7)
        g.addUndirectedEdge(0,1,10)
        g.addUndirectedEdge(0,2,10)
        g.addUndirectedEdge(0,3,10)
        g.addUndirectedEdge(2,4,30)
        g.addEdge(1,5,10)
        g.addEdge(1,2,20)
        g.addEdge(7,6)
        for i,ans in enumerate(answer):
            self.assertEqual(g.dft(i),ans)

    @weight(1)
    def test_case10(self):
        """02 Graph: BFT 1"""
        answer = [[0, 1, 2, 3],
                  [1, 0, 2, 3],
                  [2, 0, 1, 3],
                  [3]]

        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addUndirectedEdge(0,1,10)
        g.addEdge(1,3,10)
        g.addUndirectedEdge(0,2,30)
        g.addEdge(1,2,20)
        for i,ans in enumerate(answer):
            self.assertEqual(g.bft(i),ans)

    @weight(1)
    def test_case11(self):
        """02 Graph: BFT 2"""
        answer = [[0, 1, 2, 3, 4, 5],
                 [1, 0, 2, 3, 4, 5],
                 [2, 0, 4, 1, 3, 5],
                 [3, 0, 1, 2, 4, 5],
                 [4, 2, 5, 0, 1, 3],
                 [5],
                 [6],
                 [7, 6]]
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addVertex(4)
        g.addVertex(5)
        g.addVertex(6)
        g.addVertex(7)
        g.addUndirectedEdge(0,1,10)
        g.addUndirectedEdge(0,2,10)
        g.addUndirectedEdge(0,3,10)
        g.addUndirectedEdge(2,4,30)
        g.addEdge(4,5,10)
        g.addEdge(1,2,20)
        g.addEdge(7,6)
        for i,ans in enumerate(answer):
            self.assertEqual(g.bft(i),ans)

    @weight(0.5)
    def test_case12(self):
        """02 Graph: isDirected 1"""
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addEdge(0,1,10)
        g.addEdge(1,0,10)
        g.addUndirectedEdge(0,2,10)
        g.addUndirectedEdge(0,3,10)
        self.assertFalse(g.isDirected())
        g.addEdge(1,2,10)
        self.assertTrue(g.isDirected())

    @weight(0.5)
    def test_case13(self):
        """02 Graph: isDirected 2"""
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addEdge(0,1,10)
        g.addEdge(1,0,10)
        g.addUndirectedEdge(0,2,10)
        g.addUndirectedEdge(0,3,10)
        self.assertFalse(g.isDirected())
        g.addEdge(1,2,10)
        self.assertTrue(g.isDirected())

    @weight(0.5)
    def test_case14(self):
        """02 Graph: isCyclic (Undirected Graph)"""
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addUndirectedEdge(0,1,10)
        g.addUndirectedEdge(0,2,10)
        g.addUndirectedEdge(0,3,10)
        self.assertFalse(g.isCyclic())
        g.addUndirectedEdge(1,3,10)
        self.assertTrue(g.isCyclic())

    @weight(0.5)
    def test_case15(self):
        """02 Graph: isCyclic (Directed Graph)"""
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addEdge(0,1,10)
        g.addEdge(0,2,10)
        g.addEdge(1,2,10)
        self.assertFalse(g.isCyclic())
        g.addEdge(1,0,10)
        self.assertTrue(g.isCyclic())


    @weight(0.5)
    def test_case16(self):
        """02 Graph: isConnected (Undirected Graph)"""
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addUndirectedEdge(0,1,10)
        g.addUndirectedEdge(0,2,10)
        g.addUndirectedEdge(0,3,10)
        self.assertTrue(g.isConnected())
        g.addVertex(4)
        self.assertFalse(g.isConnected())

    @weight(0.5)
    def test_case17(self):
        """02 Graph: isTree"""
        g = Graph()
        g.addVertex(0)
        g.addVertex(1)
        g.addVertex(2)
        g.addVertex(3)
        g.addUndirectedEdge(0,1,10)
        g.addUndirectedEdge(0,2,10)
        g.addUndirectedEdge(0,3,10)
        self.assertTrue(g.isTree())
        g.addVertex(4)
        self.assertFalse(g.isTree())
        g.addUndirectedEdge(4,0,10)
        self.assertTrue(g.isTree())
        g.addUndirectedEdge(4,3,10)
        self.assertFalse(g.isTree())

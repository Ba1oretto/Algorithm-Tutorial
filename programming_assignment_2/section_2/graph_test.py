from programming_assignment_2.assignment_syllabus.graph import Graph, Edge

if __name__ == '__main__':
    g = Graph()
    g.addVertex(0)
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addUndirectedEdge(0,1,10)
    g.addUndirectedEdge(0,2,10)
    g.addUndirectedEdge(0,3,10)
    print(g.isTree())  # true
    g.addVertex(4)
    print(g.isTree())  # false
    g.addUndirectedEdge(4,0,10)
    print(g.isTree())  # true
    g.addUndirectedEdge(4,3,10)
    print(g.isTree())  # false


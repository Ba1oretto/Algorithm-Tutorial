from programming_assignment_2.assignment_syllabus.graph import Graph

if __name__ == '__main__':
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

    # print(g.neighbors(0))  # [1, 2, 3] [1, 2, 3]
    # print(g.neighbors(1))  # [0, 2] [2, 3, 0, 2]
    # print(g.neighbors(2))  # [0, 4] [3, 0, 2, 0, 4]
    # print(g.neighbors(3))  # [0] [0, 2, 0, 4, 0]
    # print(g.neighbors(4))  # [2, 5] [0, 2, 5]
    # print(g.neighbors(5))  # [] []

    for i,ans in enumerate(answer):
        print(g.bft(i), ans)

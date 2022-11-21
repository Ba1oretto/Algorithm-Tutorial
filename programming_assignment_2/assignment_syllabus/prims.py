import json
import random

from programming_assignment_2.assignment_syllabus.graph import Graph


def prim(graph):
    # T is empty list
    T = []

    # start function with choosing random vertex
    # however the random position can give rise same answer
    src = graph.V()[0]

    # U indicate list/set for src ←

    U = [src]

    """
           findSmallestWeightNeighbors () -> return edge
           add edge to T abd U
           remove dest from V
    """
    # while length of U not same graph.V()
    while len(U) != len(graph.V()):
        result = findSmallestEdge(U, graph)
        T.append(result)
        U.append(result[1])

    return T


def findSmallestEdge(U, g):
    edges = []

    # storage all related non repeat edge (1-4),(4-1) for example in edges[]
    for src, dest, weight in g.E():
        if src in U and dest not in U:
            # if related (connected) to the pre-vertex then add it to edges[]
            edges.append([src, dest, weight])

    # set compare cache in order to prepare compare
    minSrc = edges[0][0]
    minDest = edges[0][1]
    minWeight = edges[0][2]

    # transverse all element in edge compare with cache
    for src, dest, weight in edges:
        # if one element in edge is smaller than cache, we replace it with new minimum value
        if weight < minWeight:
            minSrc = src
            minDest = dest
            minWeight = weight
    # after transverse all element we return least weight edge
    return [minSrc, minDest, minWeight]


"""

    prototype function 
    but can not handle multiple input value of vertex

"""


def findSmallestWeightNeighbors(vertex, graph, hadView: list) -> tuple:
    neighborVertex = graph.neighbors(vertex)  # [v3, v4, v2]

    # Return a list of all edges, defined as a list of 3-tuples (src, dest, weight).
    graphEdge: tuple = graph.E()  # [(src, dest, weight),(src, dest, weight),(src, dest, weight),(src, dest, weight)]
    cachedWeight = None
    cachedEdge = None
    for singleEdge in graphEdge:  # (src, dest, weight)
        for singleNeighborVertex in neighborVertex:  # v3
            # (src, dest, weight)
            if singleEdge[0:2] == [vertex, singleNeighborVertex] and cachedWeight is None:
                # if we found correspond
                # edge we cache weight
                cachedWeight = singleEdge[2]  # set weight
                cachedEdge = singleEdge
            if singleEdge[0:2] == [vertex, singleNeighborVertex] and singleEdge[2] < cachedWeight:
                cachedWeight = singleEdge[2]  # set weight
                cachedEdge = singleEdge

    return cachedEdge


if __name__ == '__main__':
    g = Graph()
    g.addVertex('v1')
    g.addVertex('v2')
    g.addVertex('v3')
    g.addVertex('v4')
    g.addVertex('v5')
    g.addVertex('v6')
    g.addVertex('v7')

    g.addUndirectedEdge('v1', 'v2', 2)
    g.addUndirectedEdge('v1', 'v3', 4)
    g.addUndirectedEdge('v1', 'v4', 1)
    g.addUndirectedEdge('v3', 'v4', 2)
    g.addUndirectedEdge('v2', 'v4', 3)
    g.addUndirectedEdge('v3', 'v6', 5)
    g.addUndirectedEdge('v6', 'v4', 8)
    g.addUndirectedEdge('v2', 'v5', 10)
    g.addUndirectedEdge('v5', 'v4', 7)
    g.addUndirectedEdge('v5', 'v7', 6)
    g.addUndirectedEdge('v7', 'v4', 4)
    g.addUndirectedEdge('v6', 'v7', 1)

print(findSmallestEdge(['v1'], g))


def runPrim():
    with open('data.json', 'r') as file:
        data = json.load()

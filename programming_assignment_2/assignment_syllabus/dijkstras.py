import json
from graph import Graph
from queue import PriorityQueue

inf = float('inf')


def dijkstras(graph, src):
    queue = PriorityQueue()
    queue.put((0, src))

    costList = {k: 0 if k == src else inf for k in graph.V()}

    explored = {k: False for k in graph.V()}

    while not queue.empty():
        cost, vertex = queue.get()

        if explored[vertex]:
            continue

        explored[vertex] = True

        for neighbor in graph.neighbors(vertex):
            new_cost = cost + graph.matrix[graph.vertexTracker[vertex]][graph.vertexTracker[neighbor]]
            old_cost = costList[neighbor]
            costList[neighbor] = new_cost if new_cost < old_cost else old_cost
            queue.put((new_cost, neighbor))

    return costList


def runDijkstras():
    with open("P:/course/python/edu_ucdavis/programming_assignment_2/assignment_syllabus/tests/data.json") as file:
        data = json.load(file)

    graph = Graph()
    for k in data:
        graph.addVertex(k)

    for k, (v1, v2) in data.items():
        for i, (j1, j2) in data.items():
            if k == i:
                continue
            graph.addUndirectedEdge(k, i, pow(pow((v1 - j1), 2) + pow((v2 - j2), 2), 0.5))

    ret = {}
    for k in data:
        ret[k] = dijkstras(graph, k)

    return ret

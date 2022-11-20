class Graph:
    def __init__(self):
        self.vertexTracker = dict()
        self.indexMapper = list()
        self.edges = list()
        self.matrix = list()
        self.length = 0

    def addVertex(self, data):
        self.indexMapper.append(data)
        self.vertexTracker[data] = self.length
        for entry in self.matrix:
            entry.append(0)
        self.matrix.append([0 for _ in range(self.length + 1)])
        self.length += 1

    def removeVertex(self, data):
        for k in self.vertexTracker.keys():
            if self.vertexTracker[k] > self.vertexTracker[data]:
                self.vertexTracker[k] -= 1
        index = self.vertexTracker[data]
        del self.vertexTracker[data]
        self.indexMapper.remove(data)
        del self.matrix[index]
        for entry in self.matrix:
            del entry[index]

        # remove all edges that associated to the vertex
        i = 0
        for e in self.E():
            if data in e:
                del self.edges[i]
                continue
            i += 1

        self.length -= 1

    def addEdge(self, src, dest, weight=1):
        if not (src in self.vertexTracker and dest in self.vertexTracker):
            return
        self.edges.append(Edge(src, dest, weight))
        self.matrix[self.vertexTracker[src]][self.vertexTracker[dest]] = weight

    def addUndirectedEdge(self, A, B, weight=1):
        self.addEdge(A, B, weight)
        self.addEdge(B, A, weight)

    def removeEdge(self, src, dest):
        for i, e in enumerate(self.edges):
            if e[0] == src and e[1] == dest:
                del self.edges[i]
                break  # since we don't have parallel edge
        self.matrix[self.vertexTracker[src]][self.vertexTracker[dest]] = 0

    def removeUndirectedEdge(self, A, B):
        self.removeEdge(A, B)
        self.removeEdge(B, A)

    def V(self):
        return self.indexMapper

    def E(self):
        return list(e.getAsList() for e in self.edges)

    def neighbors(self, value):
        neighbor = list()
        for index, edge in enumerate(self.matrix[self.vertexTracker[value]]):
            if edge == 0:
                continue
            neighbor.append(self.indexMapper[index])
        return neighbor

    def dft(self, src):
        stack = list([src])
        seen = list()

        while stack:
            top = stack.pop()
            if top in seen:
                continue
            seen.append(top)
            neighbors = self.neighbors(top)
            for n in neighbors[::-1]:
                stack.append(n)

        return seen

    def bft(self, src):
        queue = TinyQueue(src)
        seen = list()

        while queue:
            front = queue.popleft()
            if front in seen:
                continue
            seen.append(front)
            neighbors = self.neighbors(front)
            for n in neighbors:
                queue.append(n)

        return seen

    def isDirected(self):
        pass

    def isCyclic(self):
        pass

    def isConnected(self):
        count = self.length
        root = list(i for i in range(self.length))
        rank = list(0 for _ in range(self.length))
        for edge in self.edges:
            x = self.find(root, edge[0])
            y = self.find(root, edge[1])
            if x == y:
                continue
            if rank[x] > rank[y]:
                root[y] = x
            elif rank[x] < rank[y]:
                root[x] = y
            else:
                root[x] = y
                rank[y] += 1
            count -= 1
        return count == 1

    def isTree(self):
        stack = [self.indexMapper[0]]
        seen = list()

        while stack:
            top = stack.pop()
            if top in seen:
                return False
            seen.append(top)
            for n in self.neighbors(top):
                stack.append(n)
        return len(seen) == self.length

    def __len__(self):
        return self.length

    def find(self, p, x):
        if p[x] == x:
            return x
        p[x] = self.find(p, p[x])
        return p[x]


class TinyQueue:
    def __init__(self, initial=None):
        self.length = 0
        self.head = None
        if initial is not None:
            self.length += 1
            self.head = Node(initial)
        self.tail = self.head

    def popleft(self):
        ret = None
        if self.head:
            ret = self.head.v
            next = self.head.next
            self.head = next.p(None) if next else next
            self.length -= 1
        return ret

    def append(self, value):
        node = Node(value)
        if self.head:
            self.tail = node.p(self.tail.n(node))
        else:
            self.head = self.tail = node
        self.length += 1

    # make sure while can repeatedly test the expression
    def __len__(self):
        return self.length


class Node:
    def __init__(self, value, prev=None, next=None):
        self.next = next
        self.prev = prev
        self.v: int = value

    def n(self, node):
        self.next = node
        return self

    def p(self, node):
        self.prev = node
        return self

    def __repr__(self):
        return str((self.v, self.prev.v if self.prev else None, self.next.v if self.next else None))


class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight

    def __getitem__(self, item):
        return self.u if item == 0 else self.v if item == 1 else self.weight

    def __contains__(self, item):
        return self.u == item or self.v == item

    def __repr__(self):
        return f"[{self.u}, {self.v}, {self.weight}]"

    def getAsList(self):
        return [self.u, self.v, self.weight]

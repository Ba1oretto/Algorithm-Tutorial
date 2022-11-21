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
        for i, (_, u, v, *_) in enumerate(self.edges):
            if u == src and v == dest:
                del self.edges[i]
                break  # since we don't have parallel edge
        self.matrix[self.vertexTracker[src]][self.vertexTracker[dest]] = 0

    def removeUndirectedEdge(self, A, B):
        self.removeEdge(A, B)
        self.removeEdge(B, A)

    def V(self):
        return self.indexMapper

    def E(self):
        return list(e for *_, e in self.edges)

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
        for _, u, v, *_ in self.edges:
            if not self.matrix[self.vertexTracker[v]][self.vertexTracker[u]]:
                return True
        return False

    def isCyclic(self):
        for k, v in enumerate(self.vertexTracker):
            stack = [k]
            seen = [False for _ in range(self.length)]
            first = True
            prev = None
            while stack:
                top = stack.pop()
                if not first and top == k:
                    return True
                else:
                    first = False
                if seen[self.vertexTracker[top]]:
                    continue
                seen[self.vertexTracker[top]] = True
                update = False
                for n in self.neighbors(top):
                    if n == prev:
                        continue
                    stack.append(n)
                    update = True
                if self.isDirected():
                    prev = top
                elif update:
                    prev = top
            return False

    def isConnected(self):
        count = self.length
        root = list(i for i in range(self.length))
        rank = list(0 for _ in range(self.length))
        for _, u, v, *_ in self.edges:
            x = self.find(root, u)
            y = self.find(root, v)
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
        length = round(len(self.edges) / 2)
        if length != self.length - 1:
            return False

        edgesCopy = []
        for i, (e, *_) in enumerate(self.edges):
            if not i & 1:
                edgesCopy.append(e)

        root = [i for i in range(length + 1)]
        rank = [0 for _ in range(length + 1)]

        for _, u, v, *_ in iter(edgesCopy):
            x = self.find(root, self.vertexTracker[u])
            y = self.find(root, self.vertexTracker[v])

            if x == y:
                return False

            if rank[x] > rank[y]:
                root[y] = x
            elif rank[x] < rank[y]:
                root[x] = y
            else:
                root[x] = y
                rank[y] += 1

        return True

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

    def __contains__(self, item):
        return self.u == item or self.v == item

    def __repr__(self):
        return f"[{self.u}, {self.v}, {self.weight}]"

    def __iter__(self):
        yield self
        yield self.u
        yield self.v
        yield self.weight
        yield self.getAsList()

    def getAsList(self):
        return [self.u, self.v, self.weight]

# To check if there's a cycle in Directed Graph

from collections import defaultdict


class Graph():
    def __init__(self, vertices):
        # Graph Constructor

        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):

        # Adding edges to graph
        self.graph[u].append(v)

    def isCyclicUtil(self, v, visited, recStack):

        # Marks current node as visited and adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours if any neighbour is visited and in recStack then graph is cyclic

        for neighbour in self.graph[v]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recStack):
                    return True
            elif recStack[neighbour]:
                return True

        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True
        return False


vertices = int(input("Please enter the number of vertices : "))

g = Graph(vertices)

for i in range(vertices):
    x = input("Enter connections of Vertex " + str(i) + " as equally spaced integers : ")
    x = x.split()
    x = [int(j) for j in x]
    for j in x:
        g.addEdge(i, j)

if g.isCyclic() == 1:
    print("\nGraph has a cycle")
else:
    print("\nGraph has no cycle")
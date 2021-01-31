# Python program to print DFS traversal from a given
# given graph
from collections import defaultdict

# This class represents a directed graph using adjacency
# list representation


class Graph:

    def __init__(self, vertices):

        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search
    # from given source 'src'
    def DLS(self, src, target, maxDepth):

        if src == target:
            return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0:
            return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if(self.DLS(i, target, maxDepth-1)):
                return True
        return False

    # IDDFS to search if target is reachable from v.
    # It uses recursive DLS()
    def IDDFS(self, src, target, maxDepth):

        # Repeatedly depth-limit search till the
        # maximum depth
        for i in range(maxDepth):
            if (self.DLS(src, target, i)):
                return True
        return False


# Create a graph given in the above diagram
g = Graph(8)
g.addEdge("Arad", "Timi")
g.addEdge("Arad", "sib")
g.addEdge("Arad", "Zeri")
g.addEdge("Timi", "Lug")
g.addEdge("sib", "Rim")
g.addEdge("sib", "fag")
g.addEdge("sib", "Ora")
g.addEdge("Zeri", "Ora")

target = "Rim"
maxDepth = 3
src = "Arad"

if g.IDDFS(src, target, maxDepth) == True:
    print("Reached")
else:
    print("Not Reachable")

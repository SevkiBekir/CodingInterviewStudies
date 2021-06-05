from Utils.Graph import Graph

def isRouteBetween(fromVertex, toVertex, graph):
    path = graph.searchWrtBfs(fromVertex)
    if toVertex in path:
        return True
    else:
        return False



if __name__ == '__main__':
    g1 = Graph()
    g1.insertVertex(1)
    g1.insertVertex(2)
    g1.insertVertex(3)
    g1.insertVertex(4)
    g1.construct()
    g1.print()

    g1.addEdge(1,3)
    g1.addEdge(3,2)
    # g1.addEdge(2,1)
    g1.addEdge(2,4)
    g1.print()

    fromVertex = 1
    toVertex = 4
    result = isRouteBetween(fromVertex,toVertex,g1)

    print("Route between " + str(fromVertex) + "-" + str(toVertex) + ": " + str(result))
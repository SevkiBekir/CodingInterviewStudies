from Utils.Graph import Graph

def removeBeforeAddedIntoOrderList(orderList, allVerticesForNoIncomingEdges):
    toRemoveVertexList = []
    for vertex in allVerticesForNoIncomingEdges:
        if vertex.data in orderList:
            toRemoveVertexList.append(vertex)

    for removingVertex in toRemoveVertexList:
        allVerticesForNoIncomingEdges.remove(removingVertex)

    return allVerticesForNoIncomingEdges

def buildOrder(graph):
    orderList = []
    result = graph.getAllVerticesForNoIncomingEdges()
    while result:
        print(result)
        for vertex in result:
            orderList.append(vertex.data)
        graph.removeAllVerticesForIncomingEdges(result)
        result = graph.getAllVerticesForNoIncomingEdges()
        result = removeBeforeAddedIntoOrderList(orderList,result)

    return orderList

def printOrder(orderList):
    for order in orderList:
        print(order,end=",")

    print("")

if __name__ == '__main__':
    g1 = Graph()
    g1.insertVertex("a")
    g1.insertVertex("b")
    g1.insertVertex("c")
    g1.insertVertex("d")
    g1.insertVertex("e")
    g1.insertVertex("f")
    g1.construct()
    g1.print()

    g1.addEdge("a","d")
    g1.addEdge("f","a")
    g1.addEdge("f","b")
    g1.addEdge("d","c")
    g1.addEdge("b","d")
    g1.print()

    orderList = buildOrder(g1)
    printOrder(orderList)


    g2 = Graph()
    g2.insertVertex("a")
    g2.insertVertex("b")
    g2.insertVertex("c")
    g2.insertVertex("d")
    g2.insertVertex("e")
    g2.insertVertex("f")
    g2.construct()
    g2.print()

    g2.addEdge("a","d")
    g2.addEdge("f","e")
    g2.addEdge("d","b")
    g2.addEdge("e","b")
    g2.addEdge("e","c")
    g2.addEdge("c","a")
    g2.print()

    orderList = buildOrder(g2)
    printOrder(orderList)



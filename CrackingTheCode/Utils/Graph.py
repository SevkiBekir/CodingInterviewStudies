from Utils.Queue import Queue
from Utils.Vertex import Vertex


class Graph:
    def __init__(self, isUndirected=False):
        self.size = 0
        self.vertices = []
        self.adjacencyMatrix = []
        self.isUndirected = isUndirected

    def insertVertex(self, vertexData):
        newVertex = Vertex(vertexData)

        self.vertices.append(newVertex)
        self.size += 1

    def construct(self):
        # generate adj matrix
        self.adjacencyMatrix.clear()
        for i in range(self.size):
            row = [0] * self.size
            self.adjacencyMatrix.append(row)

    def print(self):
        print("##################")
        print("# Printing Graph #")
        print("##################")
        print("From / To - >")
        print("|")
        print("v")
        rowHeader = "\t"
        splitter = ""
        for i in range(self.size):
            rowHeader += str(self.vertices[i].data) + " \t"
            splitter += "-----"
        print(rowHeader)
        print(splitter)

        for i in range(self.size):
            row = str(self.vertices[i].data) + " |\t"
            for j in range(self.size):
                row += str(self.adjacencyMatrix[i][j]) + "\t"
            print(row)

        print(splitter)

    def findIndex(self, vertexData):
        for i in range(self.size):
            if self.vertices[i].data is vertexData:
                return i

        print("Error! Not found the vertex {" + str(vertexData) + "}")
        return None

    def addEdge(self, source, destination):
        sourceIndex = self.findIndex(source)
        destionationIndex = self.findIndex(destination)

        self.adjacencyMatrix[sourceIndex][destionationIndex] = 1

        if self.isUndirected:
            self.adjacencyMatrix[destionationIndex][sourceIndex] = 1

    def getAdjcancies(self, vertexData):
        vertexIndex = self.findIndex(vertexData)
        adjcancies = []
        for i in range(self.size):
            if self.adjacencyMatrix[vertexIndex][i] == 1:
                adjcancies.append(self.vertices[i].data)

        return adjcancies

    def convertVisitedVertexToData(self,visitedVertex):
        conversion = []
        for index in range(len(visitedVertex)):
            if visitedVertex[index]:
                conversion.append(self.vertices[index].data)

        return conversion


    def searchWrtBfs(self, startingVertexData):
        visited = [False] * self.size
        queue = Queue()

        queue.enqueue(startingVertexData)

        while not queue.isEmpty():
            vertexData = queue.dequeue().data
            vertexIndex = self.findIndex(vertexData)
            visited[vertexIndex] = True

            vertexAdjcencies = self.getAdjcancies(vertexData)

            for adjVertex in vertexAdjcencies:
                adjVertexIndex = self.findIndex(adjVertex)
                if not visited[adjVertexIndex]:
                    visited[adjVertexIndex] = True
                    queue.enqueue(adjVertex)

        convertedVisitedData = self.convertVisitedVertexToData(visited)
        return convertedVisitedData


    def getFirstPathWrtDfs(self, startingVertex):
        visited = [False] * self.size
        return self.dfsHelperForFirstPath(startingVertex,visited,[])


    def dfsHelperForFirstPath(self, vertex, visitedInfo,visitedVertices):

        vertexIndex = self.findIndex(vertex.data)

        visitedInfo[vertexIndex] = True
        visitedVertices.append(vertex.data)
        #print(vertex.data, end=' ')


        vertexAdjcencies = self.getAdjcancies(vertex.data)
        for adjVertex in vertexAdjcencies:
            adjVertexIndex = self.findIndex(adjVertex)
            if not visitedInfo[adjVertexIndex]:
                return self.dfsHelperForFirstPath(self.vertices[adjVertexIndex],visitedInfo,visitedVertices)

        print("first path:")
        print(visitedVertices)
        return visitedVertices

    def getVertexForIncomingEdges(self, vertex):
        vertexIndex = self.findIndex(vertex.data)
        adjcancies = []
        for i in range(self.size):
            if self.adjacencyMatrix[i][vertexIndex] == 1:
                adjcancies.append(self.vertices[i].data)

        return adjcancies

    def getAllVerticesForNoIncomingEdges(self):
        vertices = []
        for vertex in self.vertices:
            vertexAdjcencies = self.getVertexForIncomingEdges(vertex)
            if not vertexAdjcencies:
                vertices.append(vertex)


        return vertices


    def removeIncomingEdgesFor(self, vertex):
        vertexIndex = self.findIndex(vertex.data)
        for i in range(self.size):
            if self.adjacencyMatrix[vertexIndex][i] == 1:
                self.adjacencyMatrix[vertexIndex][i] = 0

    def removeAllVerticesForIncomingEdges(self,vertexList):
        for vertex in vertexList:
            self.removeIncomingEdgesFor(vertex)

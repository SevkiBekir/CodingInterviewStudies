from Utils.BinaryTreeNode import BinaryTreeNode
from Utils.LinkedList import LinkedList
from Utils.Queue import Queue
from Utils.Tree import Tree


class BinaryTree(Tree):
    def __init__(self):
        super().__init__()
        self._size = 0

    def constructBstWith(self, sortedList):
        self.root = self._sortedListToBst(sortedList)
        self._size = len(sortedList)
        print("BST from SortedList was created")

    def _sortedListToBst(self, sortedList):
        if not sortedList:
            return None

        listSize = len(sortedList)
        mid = int(listSize / 2)
        leftNode = self._sortedListToBst(sortedList[:mid])
        root = BinaryTreeNode(sortedList[mid])
        rightNode = self._sortedListToBst(sortedList[mid + 1:])

        root.left = leftNode
        root.right = rightNode

        return root

    def printPreOrder(self, node):
        if not node:
            return

        print(node.data)
        self.printPreOrder(node.left)
        self.printPreOrder(node.right)

    def printPostOrder(self, node):
        if not node:
            return

        self.printPreOrder(node.left)
        self.printPreOrder(node.right)
        print(node.data)

    def printInOrder(self, node):
        if not node:
            return

        self.printPreOrder(node.left)
        print(node.data)
        self.printPreOrder(node.right)

    def constructBtWrt(self, dataList):
        self.root = self._sortedListToBst(dataList)
        self._size = len(dataList)
        print("binary tree was created")

    def _isVisited(self, node, visitedNodePairList):
        for nodePair in visitedNodePairList:
            if nodePair[0] == node:
                return nodePair[1]

        return None

    def _createDepthNodePair(self, node,depth):
        return [node, depth]

    def _createVisitedNodePair(self, node):
        return [node, False]

    def _isFoundNode(self, node, visitedNodePairList):
        for nodePair in visitedNodePairList:
            if nodePair[0] == node:
                return True

        return False

    def _createLinkedList(self,dataList):
        linkedList = LinkedList()

        for i in dataList:
            linkedList.insertTail(i)

        return linkedList

    def _constructHashTableForDepthNode(self):
        traversePairList = self.traverseWrtBfs()

        hashTable = {}
        for pair in traversePairList:
            if pair[1] not in hashTable.keys():
                hashTable[pair[1]] = []

            hashTable[pair[1]].append(pair[0].data)

        return hashTable

    def getDepthLinkedLists(self):
        hashTable = self._constructHashTableForDepthNode()
        depthHashTable = {}
        for depth in range(len(hashTable)):
            depthLinkedList = self._createLinkedList(hashTable[depth])
            depthHashTable[depth] = depthLinkedList

        return depthHashTable


    def traverseWrtBfs(self):
        queue = Queue()

        depth = 0
        depthNode = self._createDepthNodePair(self.root, depth)
        queue.enqueue(depthNode)
        traverseList = []
        while not queue.isEmpty():
            node = queue.dequeue().data
            traverseList.append(node)

            if node[0].left:
                depthNode = self._createDepthNodePair(node[0].left, node[1]+1)
                queue.enqueue(depthNode)

            if node[0].right:
                depthNode = self._createDepthNodePair(node[0].right, node[1]+1)
                queue.enqueue(depthNode)


            # visited[vertexIndex] = True

            # vertexAdjcencies = self.getAdjcancies(vertexData)
            #
            # for adjVertex in vertexAdjcencies:
            #     adjVertexIndex = self.findIndex(adjVertex)
            #     if not visited[adjVertexIndex]:
            #         visited[adjVertexIndex] = True
            #         queue.enqueue(adjVertex)

        # convertedVisitedData = self.convertVisitedVertexToData(visited)
        return traverseList

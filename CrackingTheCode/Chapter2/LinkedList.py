from Chapter2.Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        printingNode = self.head

        while printingNode is not None:
            print(printingNode.data)
            printingNode = printingNode.next

    def insertTail(self,newData):
        newNode = Node(newData)

        if self.head is None:
            self.head.next = newNode
            return

        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode

    def insertHead(self,newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode

    def insertNode(self,afterNode, newData):
        newNode = Node(newData)

        if afterNode is None:
            return

        nextNode = afterNode.next
        afterNode.next = newNode
        newNode.next = nextNode

    def removeNode(self,removingData):

        removingNode = self.head

        if removingNode is not None:
            # first item to delete
            if removingNode.data == removingData:
                self.head = removingNode.next
                removingNode = None
                return

            previousNode = self.head
            while removingNode is not None:
                if removingNode.data == removingData:
                    previousNode.next = removingNode.next
                    removingNode = None
                    return

                previousNode = removingNode
                removingNode = removingNode.next


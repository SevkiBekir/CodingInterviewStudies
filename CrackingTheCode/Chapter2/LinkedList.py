from Chapter2.Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def printList(self):
        print("Printing List")
        printingNode = self.head

        while printingNode is not None:
            print(printingNode.data)
            printingNode = printingNode.next

    def insertTail(self,newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            self.size +=1
            return

        lastNode = self.head

        while lastNode.next:
            lastNode = lastNode.next

        lastNode.next = newNode
        self.size += 1

    def insertHead(self,newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
            self.size +=1
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
        self.size += 1

    def removeNode(self,removingData):

        removingNode = self.head

        if removingNode is not None:
            # first item to delete
            if removingNode.data == removingData:
                self.head = removingNode.next
                removingNode = None
                self.size -= 1
                return

            previousNode = self.head
            while removingNode is not None:
                if removingNode.data == removingData:
                    previousNode.next = removingNode.next
                    removingNode = None
                    return

                previousNode = removingNode
                removingNode = removingNode.next
                self.size -= 1


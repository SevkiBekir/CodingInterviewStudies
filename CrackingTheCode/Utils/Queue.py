from Utils.Node import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def print(self):
        print("Printing Queue")
        printingNode = self.first

        while printingNode is not None:
            print(printingNode.data)
            printingNode = printingNode.next

    def enqueue(self, newData):
        newNode = Node(newData)

        if self.first is None and self.last is None:
            # first element
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

        self.size +=1
        print("New data {"+str(newData)+"} was pushed into stack")

    def dequeue(self):
        if self.first is None and self.last is None:
            print("Error! Stack is not popped! Since it is empty")
            return

        firstNode = self.first
        self.first = self.first.next
        self.size -=1

        return firstNode

    def peek(self):
        if self.first is not None:
            return self.first
        else:
            print("Error! The queue is empty")

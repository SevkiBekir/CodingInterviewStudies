from Utils.Node import Node


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def printList(self):
        print("Printing List")
        printingNode = self.top

        while printingNode is not None:
            print(printingNode.data)
            printingNode = printingNode.next

    def isEmpty(self):
        return self.size == 0

    def pop(self):
        if self.top is None:
            print("Error! Stack is not popped! Since it is empty")
            return

        popNode = self.top
        self.top = self.top.next
        self.size -=1
        return popNode

    def push(self, newData):
        newNode = Node(newData)

        newNode.next = self.top
        self.top = newNode
        self.size +=1

        print("New data {"+str(newData)+"} was pushed into stack")

    def peek(self):
        if self.top is not None:
            return self.top
        else:
            print("Error! The stack is empty")


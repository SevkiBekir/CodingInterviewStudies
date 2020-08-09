from Utils.Node import Node
from Utils.Stack import Stack

class SortedStack(Stack):
    def __init__(self):
        super().__init__()

    def reverse(self, newData=None):

        reversedStack = Stack()
        if not newData:
            for i in range(self.size):
                reversedStack.pushNode(self.pop())
        else:
            isAddedNewNode = False
            for i in range(self.size):
                # big to small
                newNode = Node(newData)

                if newData < self.peek().data and not isAddedNewNode:
                    #insert first
                    reversedStack.pushNode(newNode)
                    isAddedNewNode = True

                reversedStack.pushNode(self.pop())
            if not isAddedNewNode:
                reversedStack.pushNode(newNode)


        return reversedStack

    def push(self,newData):
        if self.isEmpty():
            super().push(newData)
        else:
            # first reverse to generate big to small stack as regards to new data
            reversedStack = self.reverse(newData)
            self.top = reversedStack.top
            self.size = reversedStack.size
            # second again reverse to generate small to big stack
            reversedStack = self.reverse()
            self.top = reversedStack.top
            self.size = reversedStack.size


if __name__ == '__main__':
    s1 = SortedStack()
    s1.push(5)
    s1.push(15)
    s1.push(25)
    s1.print()
    s1.push(2)
    s1.print()
    s1.push(3)
    s1.print()
    s1.push(30)
    s1.print()

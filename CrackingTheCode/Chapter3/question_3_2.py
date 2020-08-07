class NodeWithMin:
    def __init__(self,data,min):
        self.data = data
        self.min = min


class StackWithMin:
    def __init__(self):
        self.stack = []


    def pop(self):
        if self.stack:
            poppedNode = self.stack.pop(0)
            return poppedNode


        return None

    def min(self):
        return self.stack[0].min

    def getMin(self, newValue):
        if self.stack:
            if newValue <= self.stack[0].min:
                return newValue
            else:
                return self.stack[0].min

        else:
            return newValue

    def push(self, newData):
        node = NodeWithMin(newData,self.getMin(newData))
        self.stack.insert(0,node)
        print(str(newData) +" the data pushed on the stack")


    def print(self):
        print("PrintingStack:")
        for i in self.stack:
            print("Value: " + str(i.data) + " -- Min:" + str(i.min))



if __name__ == '__main__':
    s1  = StackWithMin()
    s1.push(5)
    s1.print()
    s1.push(4)
    s1.print()
    s1.push(20)
    s1.print()
    print("Min:")
    print(s1.min())
    s1.pop()
    s1.print()
    s1.pop()
    s1.print()
    print("Min:")
    print(s1.min())
from Utils.Stack import Stack


class SetOfStacks:

    def __init__(self):
        self.set = []
        self.set.append(Stack())
        self.singleStackCapacity = 1


    def pop(self):
        if self.set:
            lastStack = self.set[len(self.set)-1]
            poppedNode = lastStack.pop()

            self.stackControl()
            return poppedNode

        else:
            print("The set is empty")
            return None


    def push(self, newData):
        if self.isCapacityFull():
            # add new stack
            newStack = Stack()
            newStack.push(newData)
            self.set.append(newStack)
            self.singleStackCapacity +=1
            print("New stack is created")
            print("New capacity is "+ str(self.singleStackCapacity))

        else:
            lastStackIndex = len(self.set) - 1
            self.set[lastStackIndex].push(newData)



    def stackControl(self):
        if self.set:
            lastStackIndex = len(self.set) - 1
            lastStack = self.set[lastStackIndex]
            if lastStack.isEmpty():
                self.set.remove(lastStack)
                self.singleStackCapacity -=1

    def isCapacityFull(self):
        if self.set:
            lastStackIndex = len(self.set) - 1
            lastStack = self.set[lastStackIndex]
            return lastStack.size >= self.singleStackCapacity

    def print(self):
        for i in self.set:
            i.print()




if __name__ == '__main__':
    s1 = SetOfStacks()
    s1.push(5)
    s1.push(10)
    s1.push(15)
    s1.push(25)
    s1.push(35)
    s1.print()
    s1.pop()
    s1.print()
    s1.pop()
    s1.print()
    s1.push(40)
    s1.print()
    s1.push(45)
    s1.print()
    data = s1.pop()
    s1.print()
    print("the data popped:" + str(data.data))
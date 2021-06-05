from Utils.Stack import Stack


class MyQueue:

    def __init__(self):
        self.queue = Stack()
        self.isReversed = False

    def reverse(self):
        if self.queue.isEmpty():
            return


        reversedStack = Stack()
        for i in range(self.queue.size):
            reversedStack.push(self.queue.pop().data)

        self.queue = reversedStack
        self.isReversed = not self.isReversed


    def dequeue(self):
        if not self.isReversed:
            # need to reverse to pop the first element
            self.reverse()

        if self.queue.isEmpty():
            print("Error! the queue is empty")
            return

        node = self.queue.pop()

        return node

    def enqueue(self, newData):
        if self.isReversed:
            # need to reverse to push to the last element
            self.reverse()

        self.queue.push(newData)

    def print(self):
        self.queue.print()


if __name__ == '__main__':
    q1 = MyQueue()
    q1.enqueue(5)
    q1.print()
    q1.enqueue(50)
    q1.print()
    q1.enqueue(500)
    q1.print()
    dequeuedNode = q1.dequeue()
    q1.print()
    print("the data popped:" + str(dequeuedNode.data))

    dequeuedNode = q1.dequeue()
    q1.print()
    print("the data popped:" + str(dequeuedNode.data))

    q1.enqueue(60)
    q1.print()

    dequeuedNode = q1.dequeue()
    q1.print()
    print("the data popped:" + str(dequeuedNode.data))

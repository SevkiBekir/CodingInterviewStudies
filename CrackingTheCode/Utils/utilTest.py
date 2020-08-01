from Utils.Queue import Queue
from Utils.Stack import Stack

if __name__ == '__main__':
    s1 = Stack()
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.printList()

    q1 = Queue()
    q1.enqueue(3)
    q1.enqueue(4)
    q1.enqueue(5)


    q1.printList()
    print("peek is " + str(q1.peek().data))

    n1 = q1.dequeue()
    q1.printList()
    print("dequeud node is "+ str(n1.data))

    n1 = q1.dequeue()
    q1.printList()
    print("dequeud node is "+ str(n1.data))

    n1 = q1.dequeue()
    q1.printList()
    print("dequeud node is "+ str(n1.data))
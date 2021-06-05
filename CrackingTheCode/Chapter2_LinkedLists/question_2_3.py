from Utils.LinkedList import LinkedList

if __name__ == '__main__':
    l1 = LinkedList()
    l1.insertTail(1)
    l1.insertTail(2)
    l1.insertTail(3)
    l1.insertTail(4)

    l1.printList()

    l1.removeNode(3)
    l1.printList()



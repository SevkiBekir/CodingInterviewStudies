from Utils.LinkedList import LinkedList

def convertToInteger(linkedList):
    if linkedList.head is None:
        return 0

    node = linkedList.head
    sum = 0
    step = 1

    for i in range(linkedList.size-1):
        step *=10

    while node is not None:
        sum += step*node.data
        step /=10
        node = node.next

    return int(sum)

def convertToLinkedList(number):
    linkedList = LinkedList()

    numberLength = len(str(number))

    division = 1
    for i in range(numberLength-1):
        division *=10

    for i in range(numberLength):
        data = int(number/division)
        linkedList.insertTail(data)

        number %=division
        division /=10


    return linkedList


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insertTail(1)
    l1.insertTail(2)
    l1.insertTail(3)

    l1.printList()

    l2 = LinkedList()
    l2.insertTail(3)
    l2.insertTail(2)
    l2.insertTail(1)

    l2.printList()

    l1Number = convertToInteger(l1)
    l2Number = convertToInteger(l2)

    l3 = convertToLinkedList(l1Number+l2Number)
    l3.printList()
from Utils.Node import Node
from Utils.LinkedList import LinkedList
def getLastNode(linkedList):

    node = linkedList.head

    if node is None:
        return None
    while node is not None:
        if node.next is None:
            return node
        node = node.next

def isIntersectBtw(linkedList1, linkedList2):
    lastNodeForL1 = getLastNode(linkedList1)
    lastNodeForL2 = getLastNode(linkedList2)

    return id(lastNodeForL1) == id(lastNodeForL2)

def testCaseForIntersected():
    l1 = LinkedList()

    currentNode = l1.head
    for i in range(5):
        n = Node(i)
        if currentNode is None:
            l1.head = n
            currentNode = l1.head
        else:
            currentNode.next = n
            currentNode = currentNode.next


    l1.printList()

    l2 = LinkedList()

    currentNode = l1.head
    counter = 0
    while counter < 3:
        currentNode = currentNode.next
        counter +=1

    l2.head = currentNode
    l2.printList()

    # call the functions
    result = isIntersectBtw(l1,l2)
    print("Intersect Result: " + str(result))

def testCaseForNotIntersected():
    l1 = LinkedList()
    l1.insertTail(1)
    l1.insertTail(2)
    l1.insertTail(3)

    l2 = LinkedList()
    l2.insertTail(1)
    l2.insertTail(2)
    l2.insertTail(3)

    # call the functions
    result = isIntersectBtw(l1, l2)
    print("Intersect Result: " + str(result))



if __name__ == '__main__':
    # preparing the test case for intersection
    testCaseForIntersected()
    testCaseForNotIntersected()



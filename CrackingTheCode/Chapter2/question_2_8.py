from Chapter2.Node import Node
from Chapter2.LinkedList import LinkedList

def getBeginningNodeForLoop(linkedList):
    hashTable = {}

    currentNode = linkedList.head
    if currentNode is None:
        print("linkedlist is empty")
        return None

    while currentNode is not None:
        #fill hashTable
        currentNodeId = id(currentNode)
        if currentNodeId in hashTable.keys():
            return currentNode

        hashTable[currentNodeId] = 1
        currentNode = currentNode.next





def testCaseForLoopDetection():
    #circular linkedlist

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

    currentNode.next = l1.head.next.next
    # l1.printList()


    # call the functions
    result = getBeginningNodeForLoop(l1)
    if result:
        print("Started Node for loop: " + str(result.data))



if __name__ == '__main__':
    # preparing the test case for intersection
    testCaseForLoopDetection()



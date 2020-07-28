from Chapter2.Node import Node
from Chapter2.LinkedList import LinkedList

def convertLinkedListToHashTable(linkedList):
    hashTable = {}

    node = linkedList.head

    while node is not None:
        if node.data in hashTable:
            hashTable[node.data] += 1
        else:
            hashTable[node.data] = 1

        node = node.next

    return hashTable

def createLinkedListWrt(hashTable):
    newList = LinkedList();

    for key in hashTable.keys():
        newList.insertTail(key)

    return newList


def getRemovedDuplicatesOnLinkedList(linkedList):
    hashTable = convertLinkedListToHashTable(linkedList)
    newList = createLinkedListWrt(hashTable)
    return newList



if __name__ == '__main__':
    #prepare the List

    l1 = LinkedList()
    l1.insertTail(5)
    l1.insertTail(1)
    l1.insertTail(2)
    l1.insertTail(3)
    l1.insertTail(4)
    l1.insertTail(3)
    l1.insertTail(5)

    l1.printList()

    l2 = getRemovedDuplicatesOnLinkedList(l1)
    l2.printList()
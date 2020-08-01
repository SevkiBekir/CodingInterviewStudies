from Utils.LinkedList import LinkedList


def findKthElementFromLast(kth,linkedList):

    if kth > linkedList.size or kth < 1:
        print("Out of scope")
        return None

    index = linkedList.size - kth
    kthNode = linkedList.head
    for i in range(index):
        if kthNode is not None:
            kthNode = kthNode.next

    return kthNode.data



if __name__ == '__main__':
    l1 = LinkedList()
    l1.insertTail(1)
    l1.insertTail(2)
    l1.insertTail(3)
    l1.insertTail(4)

    l1.printList()
    print("findingKthElement")
    result = findKthElementFromLast(5,l1)
    print(result)
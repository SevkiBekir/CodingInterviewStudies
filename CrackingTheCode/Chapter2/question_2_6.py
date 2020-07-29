from Chapter2.LinkedList import LinkedList

def getreversedLinkedList(linkedList):
    reversedLinkedList = LinkedList()

    node = linkedList.head
    while node is not None:
        reversedLinkedList.insertHead(node.data)
        node = node.next

    return reversedLinkedList

def isPalindrome(linkedList):
    reversedLinkedList = getreversedLinkedList(linkedList)

    node = linkedList.head
    reversedNode = reversedLinkedList.head
    while node is not None:
        if node.data is not reversedNode.data:
            return False

        node = node.next
        reversedNode = reversedNode.next

    return True


if __name__ == '__main__':
    l1 = LinkedList()
    l1.insertTail('m')
    l1.insertTail('a')
    l1.insertTail('d')
    l1.insertTail('a')
    l1.insertTail('m')

    l1.printList()

    result = isPalindrome(l1)
    print(result)

    l2 = LinkedList()
    l2.insertTail('a')
    l2.insertTail('d')
    l2.insertTail('a')
    l2.insertTail('m')

    l2.printList()

    result = isPalindrome(l2)
    print(result)


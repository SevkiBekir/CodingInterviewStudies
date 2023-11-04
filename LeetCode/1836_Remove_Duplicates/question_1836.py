# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution:

    def createHashTable(self, head: ListNode) -> dict[int,list[ListNode]]:
        hashTable = dict[int,list[ListNode]]()
        
        traverseNode = head
        while traverseNode:
            if not traverseNode.val in hashTable:
                hashTable[traverseNode.val] = [traverseNode]
            else:
                hashTable[traverseNode.val].append(traverseNode)

            traverseNode = traverseNode.next

        return hashTable

    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        hashTable = self.createHashTable(head)
        currentNode : ListNode = None
        head = None
        for nodeList in hashTable.values():
            if len(nodeList) == 1:
                if not currentNode:
                    currentNode = nodeList[0]
                    head = currentNode
                    head.next = None
                    continue

                currentNode.next = nodeList[0]

                currentNode = currentNode.next
                currentNode.next = None

        if head == None:
            return None
        
        return head

if __name__ == "__main__":
    solution = Solution()
    a = ListNode(2)
    b = ListNode(3,a)
    c = ListNode(2,b)
    d = ListNode(1,c)

    solution.deleteDuplicatesUnsorted(d)
    print(d)

    a = ListNode(2)
    b = ListNode(1,a)
    c = ListNode(1,b)
    d = ListNode(2,c)

    solution.deleteDuplicatesUnsorted(d)
    print(d)

# Definition for singly-linked list.
from typing import Optional


class ListNode:
   def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

   def __str__(self) -> str:
      text = f"({self.val}, next-> {self.next})"
      return text

        


class Solution:

   def countListSize(self, head: ListNode) -> int:
      counter = 0
      traverse_node = head
      while traverse_node:
         counter += 1
         traverse_node = traverse_node.next

      return counter
   
   def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
      listSize = self.countListSize(head)
      # print(listSize)

      deleteIndexFromBegin = listSize - n
      # print("deleteIndexFromBegin", deleteIndexFromBegin)

      # remove xth from begin
      traverse_node = head
      previous_node = head
      counter = 0
      while traverse_node:
         if listSize == 1:
            return None
         
         if deleteIndexFromBegin - 1 == -1:
            # to be deleted head
            head = head.next
            return head
         
         if counter == deleteIndexFromBegin - 1:
            break

         traverse_node = traverse_node.next
         counter += 1

      # print(traverse_node)

      # remove it
      previous_node = traverse_node
      if previous_node:
         if previous_node.next:
            deleted_note = traverse_node.next

            if deleted_note.next:
               previous_node.next = deleted_note.next
            else:
               previous_node.next = None
         del deleted_note

      return head



if __name__ == "__main__":
   solution = Solution()
   a0 = ListNode(5)
   a = ListNode(4,a0)
   b = ListNode(3,a)
   c = ListNode(2,b)
   d = ListNode(1,c)

   # solution.printList(d)
   print(d)

   d = solution.removeNthFromEnd(d, 2)
   print(d)

   a0 = ListNode(5)


   # solution.printList(d)
   print(a0)

   d = solution.removeNthFromEnd(a0, 1)
   print(d)

   a0 = ListNode(2)
   a = ListNode(1,a0)
   print(a)

   d = solution.removeNthFromEnd(a, 2)
   print(d)
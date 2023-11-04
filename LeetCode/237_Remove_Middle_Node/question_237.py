

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

   
   def deleteNode(self, node):
      """
      :type node: ListNode
      :rtype: void Do not return anything, modify node in-place instead.
      """
      traverse_node = node
      while traverse_node:
         # swap values
         next_node = traverse_node.next

         if next_node:
               # next node available
               traverse_node.val = next_node.val
               # traverse_node.next = next_node.next
               if not next_node.next:
                   traverse_node.next = None

         else:
               # next node is none
               traverse_node.next = next_node
         
         traverse_node = traverse_node.next






if __name__ == "__main__":
   solution = Solution()
   a0 = ListNode(5)
   a = ListNode(4,a0)
   b = ListNode(3,a)
   c = ListNode(2,b)
   d = ListNode(1,c)

   # solution.printList(d)
   print(d)

   solution.deleteNode(d)
   print(d)

   # a0 = ListNode(5)


   # # solution.printList(d)
   # print(a0)

   # d = solution.removeNthFromEnd(a0, 1)
   # print(d)

   # a0 = ListNode(2)
   # a = ListNode(1,a0)
   # print(a)

   # d = solution.removeNthFromEnd(a, 2)
   # print(d)
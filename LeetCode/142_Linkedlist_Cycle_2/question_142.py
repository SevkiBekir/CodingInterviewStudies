

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
   
   def convertNodetoList(self, head : Optional[ListNode]) -> list:
      traverse_node = head

      node_list = []
      while traverse_node:
         node_list.append(traverse_node.val)
         traverse_node = traverse_node.next

      return node_list
   
   
   def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
      fast_node = head
      if not fast_node:
         return None
      
      if fast_node.next:
         fast_node = fast_node.next
      slow_node = head
      cycle_start_node = head
      cycle_walk_node = None

      while fast_node and slow_node and fast_node.next:

         if fast_node == slow_node:
            break

         fast_node = fast_node.next.next
         slow_node = slow_node.next

      if not fast_node:
         return None
      
      if fast_node.next == None:
         return None

      # find the cycle detection

      cycle_walk_node = fast_node.next

      while cycle_start_node:

         if cycle_walk_node == cycle_start_node:
            return cycle_walk_node
         
         if cycle_walk_node == fast_node:
            cycle_start_node = cycle_start_node.next

         cycle_walk_node = cycle_walk_node.next
   
      return None
   


def createList(node_list):
   head = ListNode(node_list[0])
   current = head
   for node in node_list[1:]:
      current.next = ListNode(node)
      current = current.next

   return head




if __name__ == "__main__":
   solution = Solution()

   # test
   c = ListNode(2)

   solution.detectCycle(c)

   # test
   c = ListNode(2)
   d = ListNode(1,c)
   c.next = d

   solution.detectCycle(d)

   # test
   a = ListNode(-4)
   b = ListNode(0,a)
   c = ListNode(2,b)
   d = ListNode(3,c)
   a.next = c

   solution.detectCycle(d)


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

   
   def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
      first_partition_head = ListNode()
      second_partition_head = ListNode()

      current_node = head
      first_partition_current = first_partition_head
      second_partition_current = second_partition_head
      while current_node:
         
         if current_node.val < x:
            first_partition_current.next = current_node
            first_partition_current = first_partition_current.next

         else:
            second_partition_current.next = current_node
            second_partition_current = second_partition_current.next


         current_node = current_node.next

      first_partition_current.next = None
      second_partition_current.next = None
      

      head = first_partition_head.next
      if not head:
         # first partion is empty list
         head = second_partition_head.next
      else:
         first_partition_current.next = second_partition_head.next

      return head




def createList(node_list):
   head = ListNode(node_list[0])
   current = head
   for node in node_list[1:]:
      current.next = ListNode(node)
      current = current.next

   return head




if __name__ == "__main__":
   solution = Solution()

   node_list = [1]
   head = createList(node_list)

   print(head)

   head = solution.partition(head, 0)
   print(head)


   node_list = [1,4,3,2,5,2]
   head = createList(node_list)

   print(head)

   head = solution.partition(head, 3)
   print(head)

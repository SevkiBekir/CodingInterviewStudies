

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

   
   def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      sum_head = ListNode()
      
      l1_current = l1
      l2_current = l2
      sum_current = sum_head

      
      # both digit size same
      previous = sum_current
      while l1_current and l2_current:
 
         sum_addition = 0
         sum_rest = 0
         sum_value = l1_current.val + l2_current.val

         if sum_current:
            sum_value += sum_current.val

         # check additions
         if sum_value > 9:
            sum_rest = sum_value % 10
            sum_addition = sum_value // 10
         else:
            sum_rest = sum_value

         if not sum_current:
            sum_current = ListNode(sum_rest)
            sum_current.next = ListNode(sum_addition)
         else:
            sum_current.val = sum_rest
            sum_current.next = ListNode(sum_addition)


         l1_current = l1_current.next
         l2_current = l2_current.next
         previous = sum_current
         sum_current = sum_current.next


      while l1_current:
         # l1 is longest
         sum_addition = 0
         sum_rest = 0
         sum_value = l1_current.val

         if sum_current:
            sum_value += sum_current.val

         # check additions
         if sum_value > 9:
            sum_rest = sum_value % 10
            sum_addition = sum_value // 10
         else:
            sum_rest = sum_value

         if not sum_current:
            sum_current = ListNode(sum_rest)
            sum_current.next = ListNode(sum_addition)
         else:
            sum_current.val = sum_rest
            sum_current.next = ListNode(sum_addition)

         l1_current = l1_current.next
         previous = sum_current
         sum_current = sum_current.next


      while l2_current:
         # l2 is longest
         sum_addition = 0
         sum_rest = 0
         sum_value = l2_current.val

         if sum_current:
            sum_value += sum_current.val

         # check additions
         if sum_value > 9:
            sum_rest = sum_value % 10
            sum_addition = sum_value // 10
         else:
            sum_rest = sum_value

         if not sum_current:
            sum_current = ListNode(sum_rest)
            sum_current.next = ListNode(sum_addition)
         else:
            sum_current.val = sum_rest
            sum_current.next = ListNode(sum_addition)

         l2_current = l2_current.next
         previous = sum_current
         sum_current = sum_current.next

        
      if not sum_current or sum_current.val == 0:
         previous.next = None

      return sum_head



def createList(node_list):
   head = ListNode(node_list[0])
   current = head
   for node in node_list[1:]:
      current.next = ListNode(node)
      current = current.next

   return head




if __name__ == "__main__":
   solution = Solution()

   # test3
   node_list1 = [9,9,9,9,9,9,9]
   head1 = createList(node_list1)
   print(head1)

   node_list2 = [9,9,9,9]
   head2 = createList(node_list2)
   print(head2)

   sum_list = solution.addTwoNumbers(head1, head2)
   print(sum_list)

   node_list1 = [2,4,3]
   head1 = createList(node_list1)
   print(head1)

   node_list2 = [5,6,4]
   head2 = createList(node_list2)
   print(head2)

   sum_list = solution.addTwoNumbers(head1, head2)
   print(sum_list)



   # test2
   node_list1 = [0]
   head1 = createList(node_list1)
   print(head1)

   node_list2 = [0]
   head2 = createList(node_list2)
   print(head2)

   sum_list = solution.addTwoNumbers(head1, head2)
   print(sum_list)



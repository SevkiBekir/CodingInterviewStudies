

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
   
   def findIntersectionNode(self, longestHead: ListNode, shortestHead: ListNode, longestLen: int, shortestLen: int) -> ListNode:
      alone_trip = longestLen - shortestLen
      
      traverse_longest = longestHead
      traverse_shortest = shortestHead

      counter = 0
      while traverse_longest:
         # walk alone

         if counter == alone_trip:
            break

         counter += 1
         traverse_longest = traverse_longest.next

      while traverse_longest and traverse_shortest:

         if traverse_shortest == traverse_longest:
            return traverse_longest
      
         traverse_longest = traverse_longest.next
         traverse_shortest = traverse_shortest.next

      return None

         
   
   def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
      len_A = self.countListSize(headA)
      len_B = self.countListSize(headB)

      if len_A > len_B:
         return self.findIntersectionNode(headA, headB, len_A, len_B)
      else:
         return self.findIntersectionNode(headB, headA, len_B, len_A)

        
        


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
   node_list1 = [1,0,0,1]
   head1 = createList(node_list1)
   print(head1)

  

   result = solution.isPalindrome(head1)
   print(result)

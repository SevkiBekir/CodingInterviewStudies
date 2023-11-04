

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
   
   # def createHashTable(self, head: Optional[ListNode]):
   #    hash_table = {}
   #    traverse_node = head
   #    while traverse_node:
   #       if traverse_node.val in hash_table:
   #          hash_table[traverse_node.val] +=1
   #          if hash_table[traverse_node.val] > 2:
   #             return False
   #       else:
   #          hash_table[traverse_node.val] = 1

   #       traverse_node = traverse_node.next

   #    return hash_table


   # def checkPalindromeFromHashTable(self, hash_table: dict):
   #    hash_table_values_list = list(hash_table.values())
   #    count_1 = hash_table_values_list.count(1)
   #    if count_1 > 1:
   #       return False
      
   #    return True

   def convertNodetoList(self, head : Optional[ListNode]) -> list:
      traverse_node = head

      node_list = []
      while traverse_node:
         node_list.append(traverse_node.val)
         traverse_node = traverse_node.next

      return node_list
   
   def isPalindrome(self, head: Optional[ListNode]) -> bool:
      node_list = self.convertNodetoList(head)
      reverse_list = node_list.copy()
      reverse_list.reverse()
      result = node_list == reverse_list

      del reverse_list
      del node_list

      return result



      # hash_table = self.createHashTable(head)
      # if not head:
      #    return False
      
      # return self.checkPalindromeFromHashTable(hash_table)

        


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

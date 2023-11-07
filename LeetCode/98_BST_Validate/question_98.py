
from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


previous = -math.inf

class Solution:
    def createBST(self,nums: list[int], left, right) -> Optional[TreeNode]:
        if left > right:
            return None
        
        mid = int(left + (right - left) / 2)

        root = TreeNode(nums[mid])
        root.left = self.createBST(nums, left, mid - 1)
        root.right = self.createBST(nums, mid + 1, right)

        return root
    
    
    def get_height(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        return 1 + max(left_height, right_height)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        check_height_diff = abs(self.get_height(root.left) - self.get_height(root.right)) < 2
        is_balanced_left = self.isBalanced(root.left) 
        is_balanced_right = self.isBalanced(root.right) 
    
        
        return check_height_diff and is_balanced_left and is_balanced_right
       


    def traverseInOrder(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return True
        
        global previous


        left_result = self.traverseInOrder(node.left)
        if not left_result:
            return False
        
        result = previous >= node.val
        if result:
            return False

        previous = node.val

        return self.traverseInOrder(node.right)



    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        global previous 
        previous = -math.inf

        if not root:
            return True
        
        return self.traverseInOrder(root)


 


def execute_operations(operation_list, operation_value_list):
    obj = None
    results = []

    for operation, value in zip(operation_list, operation_value_list):
        if operation == "Solution":
            obj = Solution(*value)
            results.append(None)  # No return value for constructor
        else:
            method = getattr(obj, operation)
            results.append(method(*value))

    return results

def createAllOperationList(operation_list, operation_value):
   all_operation_list = []
   op_len = len(operation_list)
   for index in range(op_len):
      element = {operation_list[index] : operation_value[index]}
      all_operation_list.append(element)

   return all_operation_list

def find_difference(expected, output):
    diff = []
    for i, (e, o) in enumerate(zip(expected, output)):
        if e != o:
            diff.append((i, e, o))
    return diff



if __name__ == "__main__":

    print("==== TEST 2 ====")

    solution = Solution()
    item_list = [1]

    root = solution.createBST(item_list, 0, len(item_list) - 1)

    root = TreeNode(0)
    # root.left = TreeNode(3)
    root.right = TreeNode(-1)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(25)

    op_l = ["Solution", "isValidBST" ]
    op_v = [[], [root]]
    print(execute_operations(op_l, op_v))

    print("==== TEST 2 ====")

    solution = Solution()
    item_list = [1]

    root = solution.createBST(item_list, 0, len(item_list) - 1)

    # root = TreeNode(9)
    # root.left = TreeNode(3)
    # root.right = TreeNode(20)
    # root.right.left = TreeNode(15)
    # root.right.right = TreeNode(25)

    op_l = ["Solution", "isValidBST" ]
    op_v = [[], [root]]
    print(execute_operations(op_l, op_v))

    print("==== TEST 1 ====")

    solution = Solution()
    item_list = [3,9,20,None,None,15,7]

    root = solution.createBST(item_list, 0, len(item_list) - 1)

    root = TreeNode(9)
    root.left = TreeNode(3)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(25)

    op_l = ["Solution", "isValidBST" ]
    op_v = [[], [root]]
    print(execute_operations(op_l, op_v))



  



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
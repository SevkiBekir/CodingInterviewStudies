
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


levels = []

class Solution:
    def createBST(self,nums: list[int], left, right) -> Optional[TreeNode]:
        if left > right:
            return None
        
        mid = int(left + (right - left) / 2)

        root = TreeNode(nums[mid])
        root.left = self.createBST(nums, left, mid - 1)
        root.right = self.createBST(nums, mid + 1, right)

        return root
    
    def levelOrderHelper(self, node: Optional[TreeNode], level: int) -> None:

        if len(levels) == level:
            # create new level
            levels.append([node.val])
        else:
            levels[level].append(node.val)

        if node.left:
            self.levelOrderHelper(node.left, level + 1)

        if node.right:
            self.levelOrderHelper(node.right, level + 1)


        
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        levels.clear()
        if not root:
            return []
        
        self.levelOrderHelper(root, 0)

        return levels
        
       
      

 


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

    print("==== TEST 1 ====")

    solution = Solution()
    item_list = [3,9,20,None,None,15,7]

    root = solution.createBST(item_list, 0, len(item_list) - 1)

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    op_l = ["Solution", "levelOrder" ]
    op_v = [[], [root]]
    print(execute_operations(op_l, op_v))



  



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
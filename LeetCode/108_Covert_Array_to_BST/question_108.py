
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBST(self,nums: list[int], left, right) -> Optional[TreeNode]:
        if left > right:
            return None
        
        mid = int(left + (right - left) / 2)

        root = TreeNode(nums[mid])
        root.left = self.createBST(nums, left, mid - 1)
        root.right = self.createBST(nums, mid + 1, right)

        return root
        

    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        start = 0
        end = len(nums) - 1

        return self.createBST(nums, start, end)

        
       
      

 


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

    op_l = ["Solution", "validPath" ]
    op_v = [[], [10, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5]]
    print(execute_operations(op_l, op_v))

    print("==== TEST 1 ====")

    op_l = ["Solution", "validPath" ]
    op_v = [[], [3, [[0,1],[1,2],[2,0]], 0, 2]]
    print(execute_operations(op_l, op_v))
   
  



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)

from typing import Optional

class Solution:
    def isInLeftSide(self, nums: list[int], start, element) -> bool:
        return nums[start] <= element
    
    def bsHelper(self, nums: list[int], start, element) -> bool:
        return nums[start] != element

    def search(self, nums: list[int], target: int) -> bool:
        end = len(nums) - 1
        if end < 0:
            return False
        
        start = 0

        while start <= end:
            mid = int(start + (end-start)/2)

            if nums[mid] == target:
                return True
            
            # narraw space
            if not self.bsHelper(nums, start, target):
                start += 1 
                continue

            isPivotLeft = self.isInLeftSide(nums, start, nums[mid])
            isTargetLeft = self.isInLeftSide(nums, start, target)

            # different locations
            if isPivotLeft ^ isTargetLeft:
                if isPivotLeft:
                    start = mid + 1
                elif isTargetLeft:
                    end = mid - 1
            # same location
            else:
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1

            
        return False


        
       
      

 


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

    print("==== TEST 3 ====")

    op_l = ["Solution", "search" ]
    op_v = [[], [[2,5,6,0,0,1,2], 6]]
    print(execute_operations(op_l, op_v))
   
  



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
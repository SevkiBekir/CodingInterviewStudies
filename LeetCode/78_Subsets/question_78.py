from typing import Optional

class Solution:
   def subsets(self, nums: list[int]) -> list[list[int]]:
       result = []
       self.dfs(nums, 0, [], result)
       return result
   
   def dfs(self, nums, index, path, result):
      result.append(path)

      for i in range(index, len(nums)):
          self.dfs(nums, i+1, path + [nums[i]], result)



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

   op_l = ["Solution", "subsets" ]
   op_v = [[], [[1,2,3]]]
   print(execute_operations(op_l, op_v))



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
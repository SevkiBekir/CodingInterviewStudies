from typing import Optional

class Solution:
   def __init__(self) -> None:
      self.memo: list = None

   def tribonacci_helper(self, n: int) -> int:
      
      for i in range(3, n+1):
            self.memo[i] = self.memo[i-3] + self.memo[i-2] + self.memo[i-1]

      return self.memo[n]


   def tribonacci_dynamic(self, n: int) -> int:
      if n == 0:
            return 0
      if n == 1:
            return 1
      if n == 2:
            return 1

      self.memo = [None] * (n+1)
      
      # initials
      self.memo[0] = 0
      self.memo[1] = 1
      self.memo[2] = 1

      return self.tribonacci_helper(n)
      
   def tribonacci_memo(self, n: int) -> int:
      self.memo = [None] * (n+1)

      # initials
      self.memo[0] = 0
      self.memo[1] = 1
      self.memo[2] = 1

      return self.tribonacci_memo_helper(n)
      
   def tribonacci_memo_helper(self, n: int) -> int:
      if n == 0:
         return 0
      if n == 1:
         return 1
      if n == 2:
         return 1
      
      if not self.memo[n]:
          self.memo[n] = self.tribonacci_memo_helper(n-3) + self.tribonacci_memo_helper(n-2) + self.tribonacci_memo_helper(n-1)

      return self.memo[n]
   



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

   op_l = ["Solution", "tribonacci_dynamic" ]
   op_v = [[], [4]]
   print(execute_operations(op_l, op_v))

   op_l = ["Solution", "tribonacci_memo" ]
   op_v = [[], [4]]
   print(execute_operations(op_l, op_v))


   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
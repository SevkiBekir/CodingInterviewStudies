
from typing import Optional

class Solution:
    # def divide(self, dividend: int, divisor: int) -> int:
    #     result = 0
    #     result = self.divide_helper(dividend, divisor, dividend, result)
    #     return result

    # def divide_helper(self, dividend: int, divisor: int, left , result):
    #     if left < divisor:
    #         return result
        
    #     left -= divisor
    #     result += 1
    #     return self.divide_helper(dividend,divisor,left, result)
    
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle division by zero
        if divisor == 0:
            return 2**31 - 1
        
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        
        # Get the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= (divisor << shift):
                shift += 1
            res += 1 << (shift - 1)
            dividend -= divisor << (shift - 1)
        
        if negative:
            res = -res
        return min(max(-2147483648, res), 2147483647)

 


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

   op_l = ["Solution", "divide" ]
   op_v = [[], [10,3]]
   print(execute_operations(op_l, op_v))



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
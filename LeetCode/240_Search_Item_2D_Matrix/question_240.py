
from typing import Optional

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_len = len(matrix)
        if row_len == 0:
            return False
        
        column_len = len(matrix[0])
        column_index = 0

        if row_len == 1:
            end = column_len - 1
            while column_index <= end:
                mid = column_index + (end - column_index) // 2
                if matrix[0][mid] == target:
                    return True
                
                if matrix[0][mid] < target:
                    end = mid - 1
                else:
                    column_index = mid + 1


            

        

        row_index = row_len - 1
        column_index = 0
        while row_index > 0 and column_index < column_len:
            if matrix[row_index][column_index] > target:
                row_index -= 1
            elif matrix[row_index][column_index] < target:
                column_index += 1
            else:
                return True
            
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

    op_l = ["Solution", "searchMatrix" ]
    op_v = [[], [[[-1,3]], -1]]
    print(execute_operations(op_l, op_v))
   
  



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
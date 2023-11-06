
from typing import Optional

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if n == 0:
        #     return
        
        # if m == 0:
        #     for index in range(n):
        #         nums1[index] = nums2[index]
        #     return


        # num1_length = len(nums1)
        # num2_length = n
        
        # helper_list = []
        # for num in nums1:
        #     if num != 0:
        #         helper_list.append(num)
        
        # for num in nums2:
        #     helper_list.append(num)
        
        # starting_index = m
        # for index in range(starting_index,num1_length):
        #     nums1[index] = nums2[index - num2_length]

        
        # high = m+n-1
        # helper_left = 0
        # mid = high // 2
        # helper_right = mid + 1
        # current = 0

        # while helper_left <= mid and helper_right <= high:
        #     if helper_list[helper_left] <= helper_list[helper_right]:
        #         nums1[current] = helper_list[helper_left]
        #         helper_left += 1
        #     else:
        #         nums1[current] = helper_list[helper_right]
        #         helper_right += 1
        #     current += 1

        # remaining_index = mid - helper_left
        # for index in range(remaining_index):
        #     nums1[current + index] = helper_list[helper_left + index]

        # remaining_index = num1_length - helper_right
        # for index in range(remaining_index):
        #     nums1[current + index] = helper_list[helper_right + index]


        # return nums1

        while n > 0:
            if nums1[m - 1] > nums2[n - 1] and m > 0:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
    
        return nums1

 


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

    op_l = ["Solution", "merge" ]
    op_v = [[], [[2,0],1, [1], 1]]
    print(execute_operations(op_l, op_v))
   
    print("==== TEST 2 ====")

    op_l = ["Solution", "merge" ]
    op_v = [[], [[0],0, [1], 1]]
    print(execute_operations(op_l, op_v))
    
    print("==== TEST 1 ====")

    op_l = ["Solution", "merge" ]
    op_v = [[], [[1,2,3,0,0,0],3, [2,5,6], 3]]
    print(execute_operations(op_l, op_v))



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
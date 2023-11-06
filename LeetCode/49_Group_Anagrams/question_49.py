
from typing import Optional

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        hash_table = {}

        for word in strs:
            sorted_word = str(sorted(word))
            if not sorted_word in hash_table:
                # add
                hash_table[sorted_word] = []

            hash_table[sorted_word].append(word)


        return list(hash_table.values())
      

 


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

    op_l = ["Solution", "groupAnagrams" ]
    op_v = [[], [["eat","tea","tan","ate","nat","bat"]]]
    print(execute_operations(op_l, op_v))
   
  



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
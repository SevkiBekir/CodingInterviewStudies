
from typing import Optional

class Solution:
    def createAdjencyDict(self, n: int, edges: list[list[int]]) -> dict[int, list[int]]:
        adjencyDict = dict[int, list[int]].fromkeys(list(range(0,n)))


        for edge in edges:
            from_edge = edge[1]
            to_edge = edge[0]

            if adjencyDict[from_edge]:
                adjencyDict[from_edge].append(to_edge)
            else:
                adjencyDict[from_edge] = [to_edge]

        return adjencyDict

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if numCourses <= 0:
            return []
        
        if not prerequisites:
            return list(range(numCourses))
        
        adjencyDict = self.createAdjencyDict(numCourses,prerequisites)

        starting_vertex = 0
        final_course = numCourses - 1
        pending_list = set()
        pending_list.add(starting_vertex)
        visited_list = set()
        while pending_list:
            visited_vertex = next(iter(pending_list))
            pending_list.remove(visited_vertex)

            
            if visited_vertex in visited_list:
                continue
            

            all_adjancies = adjencyDict[visited_vertex]

            if all_adjancies:
                for adj in all_adjancies:
                    pending_list.add(adj)

            visited_list.add(visited_vertex)
            if visited_vertex == final_course:
                return list(visited_list)



        return []

        
       
      

 


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

    op_l = ["Solution", "findOrder" ]
    op_v = [[], [4, []]]
    print(execute_operations(op_l, op_v))


    print("==== TEST 1 ====")

    op_l = ["Solution", "findOrder" ]
    op_v = [[], [4, [[1,0],[2,0],[3,1],[3,2]]]]
    print(execute_operations(op_l, op_v))
   
  



   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
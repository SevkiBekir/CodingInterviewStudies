
from typing import Optional

class Solution:
    def createAdjencyDict(self, n: int, edges: list[list[int]]) -> dict[int, list[int]]:
        adjencyDict = dict[int, list[int]].fromkeys(list(range(0,n)))


        for edge in edges:
            from_edge = edge[0]
            to_edge = edge[1]

            if adjencyDict[from_edge]:
                adjencyDict[from_edge].append(to_edge)
            else:
                adjencyDict[from_edge] = [to_edge]

            # bi directional
            if adjencyDict[to_edge]:
                adjencyDict[to_edge].append(from_edge)
            else:
                adjencyDict[to_edge] = [from_edge]

        return adjencyDict

    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        adjencyDict = self.createAdjencyDict(n,edges)

        starting_vertex = source
        pending_list = set()
        pending_list.add(starting_vertex)
        visited_list = set()
        while pending_list:
            visited_vertex = pending_list.pop()

            if visited_vertex == destination:
                return True
            
            if visited_vertex in visited_list:
                continue
            

            all_adjancies = adjencyDict[visited_vertex]

            if all_adjancies:
                for adj in all_adjancies:
                    pending_list.add(adj)

            visited_list.add(visited_vertex)



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
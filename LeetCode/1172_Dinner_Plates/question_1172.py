from typing import Optional


class StackNode:
   def __init__(self, val=0):
        self.val = val

   def __str__(self) -> str:
      text = f"Stack Node: {self.val}"
      return text


class Stack:

   def __init__(self, capacity):
      self.stack = []
      self.size = 0
      self.capacity = capacity
      pass

   def push(self, val: int) -> None:
      new_node = StackNode(val)
      self.stack.append(new_node)
      self.size += 1

   def pop(self) -> int:
      if self.stack:
         self.size -= 1
         return self.stack.pop().val
      
      return -1
   
   def is_capacity_full(self) -> bool:
      return self.capacity <= self.size
   
   def is_empty(self) -> bool:
      return self.size == 0

class DinnerPlates:

   def __init__(self, capacity: int):
      self.capacity = capacity
      self.stacks = []
      self.emptyStackIndexList = []
      self.stackSize = 0
      
      
   def create_new_stack(self) -> None:
      stack = Stack(self.capacity)
      self.stacks.append(stack)
      self.stackSize += 1
      self.emptyStackIndexList.append(self.stackSize - 1)
   
   def get_available_stack_index(self) -> int:
      return min(self.emptyStackIndexList)
   
   def push_data_in_available_stack(self, val: int) -> None:
      available_stack_index = self.get_available_stack_index()
      self.stacks[available_stack_index].push(val)
      
      # check this stack is now available or not
      if self.stacks[available_stack_index].is_capacity_full():
         self.emptyStackIndexList.remove(available_stack_index)


   def push(self, val: int) -> None:
      if not self.emptyStackIndexList:
         # create a new stack with the capacity
         self.create_new_stack()

      # now ready to add value to stack
      self.push_data_in_available_stack(val)


   def pop(self) -> int:
      if self.stacks:
         stack_index = self.stackSize - 1
         popped_stack = self.stacks[stack_index] # last stack
         before_popping_is_capacity_full = popped_stack.is_capacity_full()

         node = popped_stack.pop()

         if before_popping_is_capacity_full:
            # if capacity is full, then after popping, will be available
            self.emptyStackIndexList.append(stack_index)


         # check stack is empty
         if popped_stack.is_empty():
            # remove from stacks
            self.stacks.pop()
            self.stackSize -= 1

            # update available empty stack list
            self.emptyStackIndexList.remove(stack_index)


         return node

      return -1 # if not available stacks

   def popAtStack(self, index: int) -> int:
      if self.stackSize <= index:
         # out of range
         return -1
      
      if self.stacks:
         stack_index = index
         popped_stack = self.stacks[stack_index] # get stack
         before_popping_is_capacity_full = popped_stack.is_capacity_full()

         node = popped_stack.pop()

         if before_popping_is_capacity_full:
            # if capacity is full, then after popping, will be available
            self.emptyStackIndexList.append(stack_index)


         # check stack is empty
         if popped_stack.is_empty():
            # remove from stacks
            self.stacks.remove(popped_stack)
            self.stackSize -= 1

            # update available empty stack list
            self.emptyStackIndexList.remove(stack_index)

            # update indexes grater than the stack index
            for empty_stack_index in range(len(self.emptyStackIndexList)):
               if self.emptyStackIndexList[0] > stack_index:
                  self.emptyStackIndexList[0] -= 1


         return node

      return -1 # if not available stacks

def execute_operations(operation_list, operation_value_list):
    obj = None
    results = []

    for operation, value in zip(operation_list, operation_value_list):
        if operation == "DinnerPlates":
            obj = DinnerPlates(*value)
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
   # # test 1
   # print("=== TEST 1 ===")
   # operation_list = ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
   # operation_value_list = [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]
   # all_ops = createAllOperationList(operation_list,operation_value_list)
   # dinnerPlates = DinnerPlates(2)
   # dinnerPlates.push(1)
   # dinnerPlates.push(2)
   # dinnerPlates.push(3)
   # dinnerPlates.push(4)
   # dinnerPlates.push(5)
   # result = dinnerPlates.popAtStack(0)
   # print("result", result)  
   # dinnerPlates.push(20)
   # dinnerPlates.push(21)
   # result = dinnerPlates.popAtStack(0)
   # print("result", result)  
   # result = dinnerPlates.popAtStack(2)
   # print("result", result)  

   # result = dinnerPlates.pop()
   # print("result", result)
   # result = dinnerPlates.pop()
   # print("result", result)
   # result = dinnerPlates.pop()
   # print("result", result)
   # result = dinnerPlates.pop()
   # print("result", result)
   # result = dinnerPlates.pop()
   # print("result", result)
   
  


   # # test 2
   # print("=== TEST 2 ===")
   # operation_list = ["DinnerPlates","push","push","push","push","push","popAtStack","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
   # operation_value_list =[[2],[1],[2],[3],[4],[5],[1],[1],[0],[],[],[],[],[]]
   # all_ops = createAllOperationList(operation_list,operation_value_list)

   # dinnerPlates = DinnerPlates(2)
   # dinnerPlates.push(1)
   # dinnerPlates.push(2)
   # dinnerPlates.push(3)
   # dinnerPlates.push(4)
   # dinnerPlates.push(5)
   # result = dinnerPlates.popAtStack(1)
   # print("result", result) 
   # result = dinnerPlates.popAtStack(1)
   # print("result", result)  
   # result = dinnerPlates.popAtStack(0)
   # print("result", result)  
   # result = dinnerPlates.pop()
   # print("result", result)
   # result = dinnerPlates.pop()
   # print("result", result)
   # result = dinnerPlates.pop()
   # print("result", result)
   # result = dinnerPlates.pop()
   # print("result", result)
   # result = dinnerPlates.pop()
   # print("result", result)


   # print(execute_operations(operation_list, operation_value_list))

   print("==== TEST 3 ====")

   op_l = ["DinnerPlates","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","popAtStack","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","push","pop","pop","pop","pop","pop","pop","pop","pop","pop","pop"]
   op_v = [[2],[373],[86],[395],[306],[370],[94],[41],[17],[387],[403],[66],[82],[27],[335],[252],[6],[269],[231],[35],[346],[4],[6],[2],[5],[2],[2],[7],[9],[8],[1],[474],[216],[256],[196],[332],[43],[75],[22],[273],[101],[11],[403],[33],[365],[338],[331],[134],[1],[250],[19],[],[],[],[],[],[],[],[],[],[]]
   print(execute_operations(op_l, op_v))

   expected_output = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 403, 335, 94, 82, 370, -1, 6, 346, 231, 306, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 19, 250, 1, 134, 331, 338, 365, 33, 403, 11]
   your_output = [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 403, 335, 94, 82, 370, 17, 231, -1, 346, 306, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 19, 250, 1, 134, 331, 338, 365, 33, 403, 11]

   diffs = find_difference(expected_output, your_output)
   print(diffs)
from typing import Optional


class StackNode:
   def __init__(self, val=0):
        self.val = val

   def __str__(self) -> str:
      text = f"Stack Node: {self.val}"
      return text


class Stack:

   def __init__(self):
      self.stack = []
      self.size = 0
      

   def push(self, val: int) -> None:
      new_node = StackNode(val)
      self.stack.append(new_node)
      self.size += 1

   def pop(self) -> int:
      if self.stack:
         self.size -= 1
         return self.stack.pop().val
      
      return -1
   
   def top(self) -> int:
      if self.stack:
         return self.stack[-1].val
      
      return -1
   
   def is_empty(self) -> bool:
      return self.size == 0

class MyQueue:

   def __init__(self):
      self.queue = Stack()

   def push(self, x: int) -> None:
      self.queue.push(x)

   def _reverseStack(self) -> None:
      reversedStack = Stack()

      for _ in range(self.queue.size):
         reversedStack.push(self.queue.pop())

      if not reversedStack.is_empty():
         self.queue = reversedStack

   def pop(self) -> int:
      self._reverseStack()
      pop_value = self.queue.pop()
      self._reverseStack()
      return pop_value


   def peek(self) -> int:
      self._reverseStack()
      peek_value = self.queue.top()
      self._reverseStack()
      return peek_value

   def empty(self) -> bool:
      return self.queue.is_empty()





def execute_operations(operation_list, operation_value_list):
    obj = None
    results = []

    for operation, value in zip(operation_list, operation_value_list):
        if operation == "MyQueue":
            obj = MyQueue(*value)
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

   op_l = ["MyQueue", "push", "push", "peek", "pop", "empty"]
   op_v = [[], [1], [2], [], [], []]
   print(execute_operations(op_l, op_v))


   # diffs = find_difference(expected_output, your_output)
   # print(diffs)
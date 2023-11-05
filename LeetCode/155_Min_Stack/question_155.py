from typing import Optional
import sys


class StackNode:
   def __init__(self, val=0, min=sys.maxsize):
        self.val = val
        self.min = min

   def __str__(self) -> str:
      text = f"Stack Node: {self.val}"
      return text


class MinStack:

   def __init__(self):
      self.stack = []
      pass
   
   def _getMinFromLastNode(self) -> int:
      if self.stack:
         return self.stack[-1].min
      return sys.maxsize

   def push(self, val: int) -> None:
      latest_min_value = self._getMinFromLastNode()

      min_value = min(val, latest_min_value)
      new_node = StackNode(val,min_value)
      self.stack.append(new_node)

   def pop(self) -> None:
      if self.stack:
            self.stack.pop()
         

   def top(self) -> int:
      if self.stack:
         return self.stack[-1].val
      return sys.maxsize
      
      

   def getMin(self) -> int:
      if self.stack:
         return self.stack[-1].min
      return sys.maxsize




if __name__ == "__main__":
   # test 1
   minStack = MinStack()
   minStack.push(-2)
   minStack.push(0)
   minStack.push(-3)
   result = minStack.getMin()
   print("result", result)
   minStack.pop()
   result = minStack.top()
   print("result", result)
   result = minStack.getMin()
   print("result", result)


   # test 2
   print("=== TEST 2 ===")
   ["MinStack","push","push","push","push","getMin","pop","getMin","pop","getMin","pop","getMin"]
   [[],[2],[0],[3],[0],[],[],[],[],[],[],[]]
   minStack = MinStack()
   minStack.push(2)
   minStack.push(0)
   minStack.push(3)
   minStack.push(0)
   result = minStack.getMin()
   print("result", result)
   minStack.pop()
   result = minStack.getMin()
   print("result", result)
   minStack.pop()
   result = minStack.getMin()
   print("result", result)
   minStack.pop()
   result = minStack.getMin()
   print("result", result)

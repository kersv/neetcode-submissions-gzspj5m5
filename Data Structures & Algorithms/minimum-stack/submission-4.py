class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # if minStack is empty, first val is min value
        if not self.minStack:
            self.minStack.append(val)
        # if minStack is not empty, compare last minValue to current val
        else:
            newMin = min(val,self.minStack[-1])
            self.minStack.append(newMin)


        
        
    def pop(self) -> None:
        self.stack.pop() 
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        

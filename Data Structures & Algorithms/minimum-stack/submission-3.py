class MinStack:

    def __init__(self):
        self.minStack = []
        self.minValue = []
        
    def push(self, val: int) -> None:
        self.minStack.append(val)

        if len(self.minValue) != 0:
            self.minValue.append(min(self.minValue[-1], val))
        else:
            self.minValue.append(val)

    def pop(self) -> None:
        self.minStack.pop(-1)
        self.minValue.pop(-1)

    def top(self) -> int:
        return self.minStack[-1]
        

    def getMin(self) -> int:
        return self.minValue[-1]

            

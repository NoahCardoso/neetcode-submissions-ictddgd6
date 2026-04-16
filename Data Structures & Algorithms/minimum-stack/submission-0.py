class MinStack:

    stack: List
    mini: List
    
    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.mini) == 0:
            self.mini.append(val)
        else:
            self.mini.append(min(self.mini[len(self.mini)-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.mini[len(self.mini)-1]
        
        

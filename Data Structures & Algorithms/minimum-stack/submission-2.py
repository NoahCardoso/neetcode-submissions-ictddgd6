import heapq as heap
class MinStack:

    def __init__(self):
        self.stack = []
        self.order = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        heap.heappush(self.order, (val, len(self.stack)-1))

    def pop(self) -> None:
        val = self.stack.pop()
        for k in range(len(self.order)):
            v, i = self.order[k]
            if i == len(self.stack) and v == val:
                del self.order[k]
                heap.heapify(self.order)
                break

    def top(self) -> int:
        print(self.order)
        print(self.stack)
        val = self.stack[-1]
        return val

    def getMin(self) -> int:
        
        v,i = self.order[0]
        
        return v

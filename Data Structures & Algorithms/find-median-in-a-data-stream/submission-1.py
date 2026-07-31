import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] #max
        self.right = [] #min

    def addNum(self, num: int) -> None:
        isMedian = self.findMedian()
        if (isMedian is None) or num <= isMedian:
            heapq.heappush(self.left, -(num))
        else:
            heapq.heappush(self.right, num)
        if len(self.left) > len(self.right) + 1:
            overflow = -(heapq.heappop(self.left))
        
            heapq.heappush(self.right, overflow)
        if len(self.left) + 1 < len(self.right):
            overflow = heapq.heappop(self.right)
            
            heapq.heappush(self.left, -(overflow))
        print(self.left)
        print(self.right)
        print("after noah")

    def findMedian(self) -> float:
        print(self.left)
        print(self.right)
        print("meow")
        if len(self.left) > len(self.right):
            return -(self.left[0])
        elif len(self.left) < len(self.right):
            return self.right[0]
        elif len(self.left) == len(self.right):
            if self.left and self.right:
                return (-(self.left[0]) + self.right[0])/2
        else:
            return None

        
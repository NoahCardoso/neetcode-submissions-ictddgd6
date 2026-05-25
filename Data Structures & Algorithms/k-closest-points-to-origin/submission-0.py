class Solution:
    import heapq
    import math
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        def dist(l1):
            x1, y1 = l1[0], l1[1]
            x2, y2 = 0, 0
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        rank = []
        heap = []
        for p in points:
            rank.append(dist(p))
            heapq.heappush(heap, (rank[-1],p))
        for i in range(k):
            k, v = heapq.heappop(heap)
            print(k)
            res.append(v)
        return res
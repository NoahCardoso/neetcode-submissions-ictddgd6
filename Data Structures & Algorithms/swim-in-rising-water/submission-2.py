import heapq
from collections import defaultdict
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adj = defaultdict(list)
        print(grid)
        N = len(grid)
        for i in range(N):
            for j in range(N):
                for di, dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                    if i+di >= N or j+dj >= N or i+di < 0 or j+dj < 0:
                        continue
                    adj[(i,j)].append((i+di,j+dj))
        
        node_to = defaultdict(lambda: int(0))
        dist_to = defaultdict(lambda: float("inf"))
        pq = []

        dist_to[(0,0)] = 0
        heapq.heappush(pq,(0,(0,0)))
        
        
        while pq != []:
            _,v = heapq.heappop(pq)
            for i,j in adj[v]:
                w = (i,j)
                if dist_to[w] > grid[i][j]:
                    dist_to[w] = grid[i][j]
                    node_to[w] = v

                    for k in range(len(pq)):
                        _,index = pq[k]
                        if index == w:
                            del pq[k]
                    heapq.heappush(pq,(dist_to[w],w))
        c = (N-1,N-1)
        res = grid[0][0]
        while node_to[c] != 0:
            c1, c2 = c
            res = max(res,grid[c1][c2])
            c = node_to[c]
        return res
                        

        
        

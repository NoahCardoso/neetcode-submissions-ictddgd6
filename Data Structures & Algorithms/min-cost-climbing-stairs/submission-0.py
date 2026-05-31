class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost)
        path = [0] * (N)
        path[0] = cost[0]
        path[1] = cost[1]
        s = 2
        for i in range(2,N):
            
            path[i] = min(path[i-1],path[i-2]) + cost[i]
            
        return min(path[-1],path[-2])
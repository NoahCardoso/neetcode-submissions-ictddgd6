class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total = 0
        if sum(gas) < sum(cost):
            return -1
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            if total < 0:
                total = 0
                start = i+1
        return start
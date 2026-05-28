
import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = -1
        h.heapify_max(nums)
        for i in range(k):
            
            res = h.heappop_max(nums)
        return res
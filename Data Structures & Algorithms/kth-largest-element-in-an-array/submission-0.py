
import heapq as h
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = -1
        for i in range(k):
            h.heapify_max(nums)
            res = h.heappop(nums)
        return res
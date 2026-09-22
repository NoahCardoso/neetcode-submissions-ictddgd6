from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = defaultdict(int)
        bestc = 0
        bestv = 0
        for e in nums:
            elements[e] += 1
            if bestc < elements[e]:
                bestc = elements[e]
                bestv = e
        return bestv

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        prev = 0
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.add(nums[i])

        return 0
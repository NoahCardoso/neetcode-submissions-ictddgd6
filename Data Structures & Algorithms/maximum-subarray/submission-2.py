class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bt = nums[0]
        for start in range(len(nums)):
            t = 0
            for end in range(start + 1, len(nums) + 1):

                subarray = nums[start:end]
                
                t += nums[end-1]
                bt = max(bt,t)
        return bt
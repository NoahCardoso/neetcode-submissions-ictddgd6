class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def backtrack(nums, sum1, sum2, s):
            if sum1 == sum2:
                return True
            elif sum1 > sum2:
                return False
            
            for i in range(s, len(nums)):
                res = backtrack(nums, sum1+nums[i], sum2-nums[i], i + 1)
                if res:
                    return True
            return False
        return backtrack(nums, 0, sum(nums), 0)

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n-1,-1,-1):
            if goal in range(i,i+1+nums[i]):
                goal = i
        return goal == 0
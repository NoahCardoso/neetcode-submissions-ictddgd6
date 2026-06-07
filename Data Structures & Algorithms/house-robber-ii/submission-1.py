class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo1 = [-1] * len(nums)
        memo2 = [-1] * len(nums)
        def dfs(i,memo,N):
            if i >= N:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = max(dfs(i + 1, memo, N), nums[i] + dfs(i + 2, memo, N))
            return memo[i]
        a = dfs(0, memo1, len(nums)-1)
        b = dfs(1, memo2, len(nums))
        return max(a, b)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        paths = []

        path = []
        def dfs(i):
            if i >= len(nums):
                if path not in paths:
                    paths.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            dfs(i+1)
        dfs(0)
        return paths
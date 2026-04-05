class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        paths = []

        path = []
        def dfs(i):
            
            paths.append(path.copy())
                
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue

                path.append(nums[j])
                dfs(j+1)
                path.pop()
            
        dfs(0)
        return paths
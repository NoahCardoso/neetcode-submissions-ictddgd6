import copy
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        paths = []
        nums = sorted(candidates)
        
        def permute(path, total, index):
            if total > target:
                return 
            if total == target:
                paths.append(path.copy())
                return
            
            for i in range(index, len(nums)):
                
                if i > index and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                permute(path,total+nums[i], i+1)
                path.pop()
                
        
        permute([],0,0)

        return paths

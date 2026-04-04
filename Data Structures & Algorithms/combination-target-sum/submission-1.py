class Solution:
    nums: List
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        paths = []
        
        self.nums = nums
        def permute(path, total, target):
            if total > target:
                return 
            if total == target:
                
                paths.append([x for x in path])
                return
            for num in self.nums:
                if total + num <= target:
                    path.append(num)
                    total += num
                    permute(path,total,target)
                    path.remove(num)
                    total -= num


        permute([],0,target)

        unique = {tuple(sorted(lst)) for lst in paths}
        result = [list(t) for t in unique]

        return result
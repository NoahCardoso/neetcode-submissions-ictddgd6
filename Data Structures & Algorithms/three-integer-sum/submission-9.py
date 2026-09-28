class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            while l < r:
                
                if i > 0 and nums[i-1] == nums[i]:
                    l+=1
                    continue
                if nums[l] + nums[r] + nums[i] == 0 and l != i and r!=i and r != l:
                    if [nums[l],nums[r],nums[i]] not in res:
                        res.append([nums[l],nums[r],nums[i]])
                    l+=1
                elif nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                else:
                    l += 1
        return res
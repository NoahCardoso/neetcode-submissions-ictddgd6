class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        seen = []
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1,N):
                    for l in range(k+1,N):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target and {nums[i], nums[j], nums[k], nums[l]} not in seen:
                            ans.append([nums[i], nums[j], nums[k], nums[l]])
                            seen.append({nums[i], nums[j], nums[k], nums[l]})
        return ans
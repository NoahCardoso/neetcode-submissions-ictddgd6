class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1] * len(nums)
        res = 1
        for i in range(1,len(nums)):
            b = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    b = max(b,arr[j])
            arr[i] = b+1
            res = max(res,arr[i])
        print(arr)
        return res

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        before = 1
        for i in range(len(nums)):
            product = before
            for j in range(i+1,len(nums)):
                product *= nums[j]
            res.append(product)
            before *= nums[i]
        return res
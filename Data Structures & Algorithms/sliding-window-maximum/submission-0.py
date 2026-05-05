class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l = 0
        r = k
        while r <= len(nums):
            window = nums[l:r]
            if window:
                v = max(window)
            output.append(v)

            l += 1
            r += 1
        return output
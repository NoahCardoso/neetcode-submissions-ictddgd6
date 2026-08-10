class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        start = k
        end = N+k
        temp = [0] * N
        for i in range(N):
            temp[i] = nums[i]
        for i in range(N):
            nums[(i+k)%N] = temp[i]


        
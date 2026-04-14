class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ls = []
        nums.sort()
        print("MEOW")
        for i in range(len(nums)):
            print(i)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l,r = i+1, len(nums)-1
            while r > l:
                three_sum = nums[l] + nums[r] + nums[i]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ls.append([nums[l],nums[r],nums[i]])
                    l+=1
                    while nums[l] == nums[l-1] and r > l:
                        l+=1
        return ls
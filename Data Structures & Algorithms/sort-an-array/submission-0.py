class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left=self.mergeSort(arr[:mid])
        right=self.mergeSort(arr[mid:])
        def merge(left: List[int],right: List[int]):
            res = []
            l = 0
            r = 0
            while l < len(left) and r < len(right):
                if left[l] <= right[r]:
                    res.append(left[l])
                    l+=1
                else:
                    res.append(right[r])
                    r+=1
            res.extend(left[l:])
            res.extend(right[r:])
            return res
        return merge(left,right)
    

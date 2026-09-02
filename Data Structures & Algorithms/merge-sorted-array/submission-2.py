class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        s = 0
        
        for i in range(m+n):
            
            while s < n and nums2[s] < nums1[i]:
                # move end of list 0 to index i
                for k in range(n+m-1,i,-1):
                    temp = nums1[k]
                    nums1[k] = nums1[k-1]
                    nums1[k-1] = temp
                #
                print(nums1)
                print(s)
                nums1[i] = nums2[s]
                s += 1
        while s < n:
            nums1[m+s] = nums2[s]
            s += 1
        print(nums1)
        

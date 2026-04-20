import bisect
class Solution:
    def trap(self, height: List[int]) -> int:
        adj_height = dict()
        for i in range(len(height)):
            l = 0
            r = 0
            
            for j in range(0, i):
                if height[j] > l:
                    l = height[j]
            for j in range(i+1,len(height)):
                if height[j] > r:
                    r = height[j]

            adj_height[i] = (l,r)
        volume = 0
        for i in range(len(height)):
            l, r = adj_height[i]
            
            v_i = min(l,r) - height[i]
            print(f"{height[i]} v{v_i}")
            if v_i > 0:
                volume += v_i
        return volume
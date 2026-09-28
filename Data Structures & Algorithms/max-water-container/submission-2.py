class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m_amount = 0
        def water(a,b):
            return min(heights[a],heights[b])*abs(a-b)
        
        l = 0
        r = len(heights) - 1 
        while l < r:
            m_amount = max(m_amount,min(heights[l],heights[r])*abs(l-r))
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return m_amount
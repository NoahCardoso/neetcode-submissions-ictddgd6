class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        
        prev = [1,1,1]
        a, b, c = target
        for i in range(n):

            ## any larger then target pass
            # if has all three return true
            # if ai, bi, ci doesnt exist then not possible 

            ai, bi, ci = triplets[i]
            
            if ai > a or bi > b or ci > c:
                continue
            ap, bp, cp = prev
            triplets[i] = [max(ap,ai),max(bp,bi),max(cp,ci)]
            prev = triplets[i]
        return prev == target
            
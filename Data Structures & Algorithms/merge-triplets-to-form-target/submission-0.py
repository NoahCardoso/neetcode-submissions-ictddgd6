class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        n = len(triplets)
        a = False
        b = False
        c = False
        for i in range(n):
            ai, bi, ci = triplets[i]
            aj, bj, cj = target
            if ai == aj: a = True
            if bi == bj: b = True
            if ci == cj: c = True
                
        if not (a and b and c):
            return False
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
            
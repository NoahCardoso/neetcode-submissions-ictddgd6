class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        
        for i in range(len(s)):
            # if i > 0:
            #     if s[i] == s[i-1]:
            #         continue
            outs = k
            r = i+1
            while r < len(s):
                if s[r] == s[i]:
                    r += 1
                    continue
                if outs == 0:
                    break
                if outs != 0 and s[r] != s[i]:
                    outs -= 1
                    r += 1
                print(f"i: {i}")
                

            
            l = i - 1
            while l >= 0:
                if s[l] == s[i]:
                    l -= 1
                    continue
                if outs == 0:
                    break
                if outs != 0 and s[l] != s[i]:
                    outs -= 1
                    l -= 1
                print(f"i: {i}")
                print(l)
            
            best = max(r-l-1,best)
        return best
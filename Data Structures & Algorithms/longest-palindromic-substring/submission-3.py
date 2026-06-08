class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.seen = set()
        N = len(s)
        if N == 1:
            return s
        l, r = 0, 0
        for i in range(N):
            for j in range(i+1, N):
                if self.isPalindrome(s[i:j+1]) and j-i > r-l:
                    l,r=i,j
        return s[l:r+1]
        
    def isPalindrome(self, s: str) -> bool:
        if s in self.seen:
            return False
        self.seen.add(s)
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c
        return newStr == newStr[::-1]
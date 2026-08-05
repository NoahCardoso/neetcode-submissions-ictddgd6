class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        best = strs[0]
        LARGE = len(strs[0])
        self.count = LARGE
        wordi = strs[0]
        for j in range(1,len(strs)):
            wordj = strs[j]
            
            mcount = 0
            for c in range(len(wordi)):
                if c < len(wordj) and wordj[c] == wordi[c]:
                    mcount += 1
                else:
                    break
            self.count = min(mcount,self.count)
            print(self.count)
            if len(best) > self.count:
                best = wordj[:self.count]
            print(best)
        return best

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lookup = self.char_freq(s1)
        for i in range(len(s2)):
            found = {}
            while i < len(s2) and s2[i] in lookup.keys() and lookup.get(s2[i],0) >= found.get(s2[i],0):
                found[s2[i]] = found.get(s2[i],0) + 1
                if lookup == found:
                    return True
                if i + 1 < len(s2):
                    i += 1
                else:
                    break

            print(found)
            if lookup == found:
                return True
        return False

    def char_freq(self,s):
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        return freq
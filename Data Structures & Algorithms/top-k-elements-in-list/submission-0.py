class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freak = dict()
        for num in nums:
            if num in freak.keys():
                freak[num] += 1
            else:
                freak[num] = 1
        result = sorted(freak, key=freak.get)
        return result[len(result)-k:]
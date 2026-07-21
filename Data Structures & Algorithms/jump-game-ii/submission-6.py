class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        def bfs(i, jumps):
            if i == len(nums) - 1:
                return jumps
            j = i + nums[i]
            
            ranki,ni = i+nums[i], i+1
            for k in range(i+1,j+1):
                print(f"{i} {k} {ranki}")
                if k >= len(nums):
                    break
                rankk = k+nums[k]
                if k == len(nums) - 1:
                    ni = k
                    break
                if rankk > ranki:
                    ranki = rankk
                    ni = k
            print(ni)
            return bfs(ni,jumps+1)
        
        return bfs(0,0)

                
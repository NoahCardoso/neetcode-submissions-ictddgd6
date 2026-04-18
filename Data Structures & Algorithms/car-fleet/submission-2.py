class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(zip(position, speed)) 
        position, speed = zip(*pairs)
        # print(position)
        for i in range(len(position)-1,-1,-1):
            rank = (target - position[i] ) / speed[i]
            if i < len(position)-1:
                infront_rank = stack.pop()
                if infront_rank >= rank:
                    stack.append(infront_rank)
                else:
                    stack.append(infront_rank)
                    stack.append(rank)
            else:
                stack.append(rank)
        return len(stack)
                
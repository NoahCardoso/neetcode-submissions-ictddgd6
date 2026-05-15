class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])
        seen = set()
        def fill(i, j):

            if i >= n or i < 0 or j < 0 or j >= m:
                return False
            if board[i][j] == "X" or (i,j) in seen : return True
            seen.add((i, j))
            return fill(i+1, j) and fill(i-1, j) and fill(i, j+1) and fill(i, j-1)


        for i in range(n):
            
            for j in range(m):
                seen.clear()
                if board[i][j] == "X": continue
                if fill(i,j): 
                    board[i][j] = "X"
        

                
        
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visit = set()
        
        def backtracking(r,c,i,string):
            
            
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or i >= len(word) or word[i] != board[r][c] or (r,c) in visit:
                return False
            
            visit.add((r,c))
            string += board[r][c]

            if string == word:
                return True

            
            if backtracking(r,c+1,i+1,string): return True
                
            if backtracking(r,c-1,i+1,string): return True
                
            if backtracking(r+1,c,i+1,string): return True
            
            if backtracking(r-1,c,i+1,string): return True
            
            visit.remove((r,c))

            return False


        for r in range(ROWS):
            for c in range(COLS):
                visit = set()
                
                if backtracking(r,c,0,""):
                    return True
        return False
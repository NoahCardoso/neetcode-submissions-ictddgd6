class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["." * n] * n
        valid_locations = []
        for i in range(n):
            row = [0] * n
            valid_locations.append(row)
        self.output = []

        def paint(matrix, x, y):
            rows = len(matrix)
            cols = len(matrix[0])

            result = [row[:] for row in matrix]

            for j in range(cols):
                result[x][j] = 1

            for i in range(rows):
                result[i][y] = 1

            directions = [
                (-1, -1),
                (-1, 1),
                (1, -1),
                (1, 1)
            ]

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                while 0 <= nx < rows and 0 <= ny < cols:
                    result[nx][ny] = 1
                    nx += dx
                    ny += dy

            return result
        def backtrack(board, valid_locations, queens, i):
            
            if queens == 0:
                
                self.output.append(board)
                return
            if i == len(board):
                return 
            n = len(board)
                
            for j in range(n):
                if valid_locations[i][j] == 0:
                    s = list(board[i])
                    s[j] = "Q"
                    board[i] = "".join(s)

                    new_valid_locations = paint(valid_locations, i, j)
                    #print(f"{k} {queens}")
                    backtrack(board.copy(), new_valid_locations, queens - 1,i+1)

                    s = list(board[i])
                    s[j] = "."
                    board[i] = "".join(s)
    
        backtrack(board, valid_locations, n, 0)
        
        return self.output
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(i, j, prev, visit):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or (i,j) in visit or prev > heights[i][j]:
                return
            visit.add((i,j))
            dfs(i+1,j,heights[i][j],visit)
            dfs(i-1,j,heights[i][j],visit)
            dfs(i,j+1,heights[i][j],visit)
            dfs(i,j-1,heights[i][j],visit)

        for i in range(ROWS):
            dfs(i, 0, heights[i][0], pacific)
            dfs(i,COLS-1, heights[i][COLS-1],atlantic)

        for j in range(COLS):
            dfs(0, j, heights[0][j], pacific)
            dfs(ROWS-1,j,heights[ROWS-1][j],atlantic)
        
        return [[i,j] for (i,j) in pacific if (i,j) in atlantic]
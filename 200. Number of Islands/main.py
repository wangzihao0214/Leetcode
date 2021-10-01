class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit(row, col, direction):
            row_new = row + direction[0]
            col_new = col + direction[1]
            
            if 0 <= row_new < m and 0 <= col_new < n: 
                if grid[row_new][col_new] == "1" and not visited[row_new][col_new]:
                    s.append((row_new, col_new))
                    visited[row_new][col_new] = True
            
        m = len(grid)
        n = len(grid[0])
        result = 0
        
        visited = [[False] * n for _ in range(m)]
        s = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    s.append((i, j))
                    while len(s):
                        row, col = s.pop()
                        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            visit(row, col, direction)
                    result += 1
        
        return result
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def visit(r, c, direction):
            dr, dc = direction[0], direction[1]
            r_new = r + dr
            c_new = c + dc
            
            if 0 <= r_new < m and 0 <= c_new < n:
                if not visited[r_new][c_new] and grid[r_new][c_new] == 1:
                    visited[r_new][c_new] = True
                    s.append((r_new, c_new)) 
                    return 1
            return 0
        
        m = len(grid)
        n = len(grid[0])
        result = 0
        
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    s = [(i, j)]
                    visited[i][j] = True
                    area = 1
                    while len(s) != 0:
                        r, c = s.pop()
                        area += visit(r, c, (0, 1)) + visit(r, c, (0, -1)) + visit(r, c, (1, 0)) + visit(r, c, (-1, 0))
                    if area > result:
                        result = area
        
        return result
        
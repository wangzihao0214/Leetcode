class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def visit(r, c, direction):
            dr, dc = direction[0], direction[1]
            r_new = r + dr
            c_new = c + dc
            
            if 0 <= r_new < m and 0 <= c_new < n:
                if not visited[r_new][c_new] and grid[r_new][c_new] == 1:
                    visited[r_new][c_new] = True
                    grid[r_new][c_new] = 2
                    temp.append((r_new, c_new)) 
        
        m = len(grid)
        n = len(grid[0])
        
        result = [[0] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        
        s = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    s.append((i, j))
                    visited[i][j] = True
                if grid[i][j] == 0:
                    visited[i][j] = True
                    
        temp = []
        result = 0
        while len(s) != 0:
            r, c = s.pop()
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                visit(r, c, direction)
            if len(s) == 0:
                if len(temp):
                    result += 1
                s = temp
                temp = []
                
        all_visited = True
        for i in range(m):
            for j in range(n):
                all_visited =  all_visited and visited[i][j]
                if not all_visited:
                    return -1
        return result
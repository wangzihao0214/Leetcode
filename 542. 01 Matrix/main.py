class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def visit(r, c, direction):
            dr, dc = direction[0], direction[1]
            r_new = r + dr
            c_new = c + dc
            
            if 0 <= r_new < m and 0 <= c_new < n:
                if not visited[r_new][c_new] and mat[r_new][c_new] != 0:
                    visited[r_new][c_new] = True
                    result[r_new][c_new] = result[r][c] + 1
                    temp.append((r_new, c_new)) 
                return mat[r_new][c_new]
            return 1
        
        m = len(mat)
        n = len(mat[0])
        
        result = [[0] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        
        s = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    s.append((i, j))
                    visited[i][j] = True
        temp = []
        while len(s) != 0:
            r, c = s.pop()
            for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                visit(r, c, direction)
            if len(s) == 0:
                s = temp
                temp = []
        
        return result
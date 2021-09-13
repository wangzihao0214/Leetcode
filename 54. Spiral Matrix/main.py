class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def visit(r, c):
            for direction in [(0, 1), (1, 0), (0, -1)]:
                r_new = r + direction[0]
                c_new = c + direction[1]
                if 0 <= r_new < m and 0 <= c_new < n and not visited[r_new][c_new]:
                    s.append((r_new, c_new))
                    result.append(matrix[r_new][c_new])
                    visited[r_new][c_new] = True
                    return
                
            r_new = r - 1
            c_new = c
            if 0 <= r_new < m and 0 <= c_new < n:
                while not visited[r_new][c_new]:
                    visited[r_new][c_new] = True
                    result.append(matrix[r_new][c_new])
                    r_new -= 1
                if c_new + 1 < n and not visited[r_new + 1][c_new + 1]:
                    s.append((r_new + 1, c_new))
        
        m = len(matrix)
        n = len(matrix[0])
        result = []
        
        s = []
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        s.append((0, 0))
        result.append(matrix[0][0])
        while len(s) != 0:
            r, c = s.pop()
            visit(r, c)
        
        return result
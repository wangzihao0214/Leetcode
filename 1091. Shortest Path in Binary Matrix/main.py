class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        result = 1
        
        layer_cur = []
        visited = [[False] * n for _ in range(n)]
        
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1
        if n == 1:
            return 1
            
        visited[0][0] = True
        layer_cur.append((0, 0))
            
        while len(layer_cur):
            layer_nxt = []
            while len(layer_cur):
                cur = layer_cur.pop(0)
                for direction in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
                    r_new = cur[0] + direction[0]
                    c_new = cur[1] + direction[1]
                    if 0 <= r_new < n and 0 <= c_new < n:
                        if grid[r_new][c_new] == 0 and not visited[r_new][c_new]:
                            visited[r_new][c_new] = True
                            layer_nxt.append((r_new, c_new))
                            if r_new == n - 1 and c_new == n - 1:
                                return result + 1
            result += 1
            layer_cur = layer_nxt
        
        return -1
    
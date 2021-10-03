class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        visited = [[False] * n for _ in range(m)]
        
        s = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and not visited[i][j]:
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        on_bound = True
                    else:
                        on_bound = False
                        
                    visited[i][j] = True
                    s.append((i, j))
                    region = []
                    while len(s):
                        cur = s.pop()
                        region.append(cur)
                        
                        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            r_new = cur[0] + direction[0]
                            c_new = cur[1] + direction[1]
                            
                            if 0 <= r_new < m and 0 <= c_new < n:
                                if board[r_new][c_new] == "O" and not visited[r_new][c_new]:
                                    s.append((r_new, c_new))
                                    visited[r_new][c_new] = True
                                    if r_new == 0 or r_new == m - 1 or c_new == 0 or c_new == n - 1:
                                        on_bound = True
                    
                    if not on_bound:
                        for pos in region:
                            board[pos[0]][pos[1]] = "X"
        
        print(board)
                          
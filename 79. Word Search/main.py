class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def visit(r, c, cnt):
            if cnt == length:
                return True
            if not visited[r][c] and board[r][c] == word[cnt]:
                visited[r][c] = True
                for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_r = r + direction[0]
                    new_c = c + direction[1]
                    if 0 <= new_r < m and 0 <= new_c < n:
                        if visit(new_r, new_c, cnt + 1):
                            return True
                visited[r][c] = False
            return False
        
        m = len(board)
        n = len(board[0])
        result = False
        length = len(word)
        print(length)
        
        if m == 1 and n == 1:
            if length == 1 and board[0][0] == word[0]:
                return True
            else:
                return False
        
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visit(i, j, 0):
                    return True
        
        return False          
                    
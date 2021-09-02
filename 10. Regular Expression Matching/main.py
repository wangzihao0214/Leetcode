class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1= len(s)
        n2 = len(p)
        
        def match(i, j):
            if i == 0:
                return False
            if p[j - 1] == ".":
                return True
            return s[i - 1] == p[j - 1]
        
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for i in range(n1 + 1):
            for j in range(1, n2 + 1):
                if p[j - 1] == "*":
                    dp[i][j] |= dp[i][j - 2]
                    if match(i, j - 1):
                        dp[i][j] |= dp[i - 1][j]
                else:
                    if match(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[n1][n2]
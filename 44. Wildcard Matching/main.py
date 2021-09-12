class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(i, j): 
            if i == 0:
                return False
            if p[j] == "?":
                return True
            return s[i] == p[j]
        
        
        s = " " + s
        p = " " + p
        n1 = len(s)
        n2 = len(p)
        
        dp = [[False] * n2 for _ in range(n1)]
        dp[0][0] = True
        
        for i in range(n1):
            for j in range(1, n2):
                if p[j] == "*":
                    dp[i][j] |= dp[i][j - 1]
                    dp[i][j] |= dp[i - 1][j]
                else:
                    if match(i, j):
                        dp[i][j] |= dp[i - 1][j - 1]
        return dp[n1 - 1][n2 - 1]
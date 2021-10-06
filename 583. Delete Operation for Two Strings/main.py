class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        
        dp = [[0] * n2 for _ in range(n1)]
        
        if word1[0] == word2[0]:
            dp[0][0] = 1
        for i in range(1, n1):
            if word1[i] == word2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n2):
            if word1[0] == word2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, n1):
            for j in range(1, n2):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return n1 + n2 - 2 * dp[n1 - 1][n2 - 1]
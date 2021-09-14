class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[] for _ in range(n)]
        dp[0].append(triangle[0][0])
        
        for i in range(1, n):
            m = len(triangle[i])
            dp[i].append( dp[i - 1][0] + triangle[i][0])
            for j in range(1, m - 1):
                dp[i].append(min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j])
            dp[i].append(dp[i - 1][m - 2] + triangle[i][m - 1])
            
        return min(dp[n - 1])
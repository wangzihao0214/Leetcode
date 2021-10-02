class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        # 反向DP
        m = len(dungeon)
        n = len(dungeon[0])
        
        dp = [[0] * n for _ in range(m)]
        
        if dungeon[m - 1][n - 1] < 0:
            dp[m - 1][n - 1] = -dungeon[m - 1][n - 1] + 1
        else:
            dp[m - 1][n - 1] = 1
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)
        
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                temp = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(temp - dungeon[i][j], 1)
        
        return dp[0][0]
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * n
        dp[0] = 1
        dp[1] = 1
        
        for w in range(2, n + 1):
            for i in range(1, w):
                temp = max(dp[w - i - 1], w - i) * i
                if temp > dp[w - 1]:
                    dp[w - 1] = temp
        
        return dp[-1]

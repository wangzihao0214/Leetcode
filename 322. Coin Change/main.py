class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [-1] * amount
        dp = [0] + dp
        
        for w in range(1, amount + 1):
            temp = float('inf')
            possible = False
            for j in range(n):
                if coins[j] <= w:
                    if dp[w-coins[j]] != -1 and temp > dp[w - coins[j]]:
                        temp = dp[w - coins[j]] + 1
                        dp[w] = temp
        
        return dp[amount]
    
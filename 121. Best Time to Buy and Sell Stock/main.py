class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        result = 0
        minimum = prices[0]
        
        for i in range(1, n):
            temp = prices[i] - minimum
            if temp > result:
                result = temp
            minimum = min(minimum, prices[i])
        
        return result
        
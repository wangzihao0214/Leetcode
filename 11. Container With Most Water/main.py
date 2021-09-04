class Solution:
    def maxArea(self, height: List[int]) -> int:
#         n = len(height)
#         dp = [[0] * n for _ in range(n)]
        
#         for i in range(n - 1):
#             dp[i][i + 1] = min(height[i], height[i + 1])
        
#         for length in range(2, n):
#             for i in range(n - length):
#                 j = i + length
#                 temp = min(height[i], height[j]) * length
#                 dp[i][j] = max(dp[i][j - 1], dp[i + 1][j], temp)
        
#         return dp[0][n - 1]
        
        n = len(height)
        left = 0
        right = n - 1
        result = 0
        
        while left < right:
            h_left = height[left]
            h_right = height[right]
            
            temp = min(h_left, h_right) * (right - left)
            if temp > result:
                result = temp
            
            if h_left < h_right:
                left += 1
            else:
                right -= 1
        
        return result
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        
        dp = [[0] * n2 for _ in range(n1)]
        
        if text1[0] == text2[0]:
            dp[0][0] = 1
        for i in range(1, n1):
            if text1[i] == text2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i - 1][0]
        for j in range(1, n2):
            if text1[0] == text2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, n1):
            for j in range(1, n2):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n1 - 1][n2 - 1]
    
#         def backtrace(path, pivot, start_index):
#             if start_index == n1 or pivot == n2:
#                 temp = len(path)
#                 if temp > self.result:
#                     self.result = temp
#                 return
#             for i in range(start_index, n1):
#                 if text1[i] == text2[pivot]:
#                     path.append(text1[i])
#                     backtrace(path, pivot + 1, i + 1)
#                     path.pop()
#             backtrace(path, pivot + 1, start_index)
        
#         n1 = len(text1)
#         n2 = len(text2)
#         self.result = 0
#         backtrace([], 0, 0)
#         return self.result
    
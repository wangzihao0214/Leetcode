class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1, 2]
        for i in range(2, n):
            result.append(result[i - 1] + result[i - 2])
        return result[n - 1]
    
#         def backtrace(n):
#             if n == 1:
#                 return 1
#             if n == 2:
#                 return 2
#             result = backtrace(n - 1) + backtrace(n - 2)
#             return result
        
#         return backtrace(n)
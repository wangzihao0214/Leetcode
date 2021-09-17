class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        f = [1] + [0] * n
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                f[i] += f[i - 1]
            if i > 1 and s[i - 2] != '0' and int(s[i-2:i]) <= 26:
                f[i] += f[i - 2]
        return f[n]

#         def backtrace(remain, result):
#             if len(remain) == 0:
#                 print(path)
#                 result.append(path[:])
#                 return
#             for right in range(0, len(remain)):
#                 num = int(remain[:right + 1])
#                 if (0 < num < 10 and right == 0) or (10<= num <= 26):
#                     path.append(num)
#                 else:
#                     return
#                 backtrace(remain[right + 1:], result)
#                 path.pop()
#             return result
                
#         path = []
#         result = []
#         backtrace(s, result)
#         return len(result)
        
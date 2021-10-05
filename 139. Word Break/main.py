class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        m = len(wordDict)
        
        minimum = 1001
        maximum = 0
        for i in range(m):
            if len(wordDict[i]) < minimum:
                minimum = len(wordDict[i])
            if len(wordDict[i]) > maximum:
                maximum = len(wordDict[i])
        
        dp = [[False] * n for _ in range(n)]
        for length in range(minimum, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i: j + 1] in wordDict:
                    dp[i][j] = True
                else:
                    for left in range(minimum, length + 1):
                        right = length - left
                        if right >= minimum:
                            dp[i][j] = dp[i][i + left - 1] and dp[i + left][i + left + right - 1]
                            if dp[i][j]:
                                break                   
        return dp[0][n - 1]

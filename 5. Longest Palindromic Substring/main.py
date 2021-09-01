class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        n = len(s)
        dp = [[False for i in range(n)] for i in range(n)]

        for i in range(n):
            dp[i][i] = True
            result = s[i]
        if n == 1:
            return result

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                result = s[i: i + 2]
        if n == 2:
            return result

        length = 3
        while length <= n:
            for left in range(n - length + 1):
                if s[left] == s[left + length - 1] and dp[left + 1][left + length - 2]:
                    dp[left][left + length - 1] = True
                    result = s[left: left + length]
            length += 1
        return result
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [None]
        dp[1] = ["()"]
        
        for i in range(2, n + 1):
            for k in range(i):
                j = i - 1 - k
                for s1 in dp[k]:
                    for s2 in dp[j]:
                        if not s1:
                            s1 = ""
                        if not s2:
                            s2 = ""
                        dp[i].append("(" + s1 + ")" + s2)

        return dp[n]
        
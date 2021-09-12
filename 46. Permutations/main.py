class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        dp = [[] for _ in range(n)]
        
        dp[0].append([nums[0]])
        
        
        for i in range(1, n):
            pos_max = len(dp[i - 1][0])
            for j in range(pos_max + 1):
                for ele in dp[i - 1]:
                    temp = ele[:j] + [nums[i]] + ele[j:]
                    dp[i].append(temp)
        return dp[n - 1]
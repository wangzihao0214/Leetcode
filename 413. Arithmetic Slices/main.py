class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return 0
        
        dp = [[False] * n for _ in range(n)]
        result = 0
        
        for i in range(n - 2):
            if nums[i + 2] - nums[i + 1] == nums[i + 1] - nums[i]:
                dp[i][i + 2] = True
                result += 1
                
        for length in range(4, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i][j - 1] and nums[j] - nums[j - 1] == nums[j - 1] - nums[j - 2]:
                    dp[i][j] = True
                    result += 1
        
        return result
                    
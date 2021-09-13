class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        
        if n == 1:
            return True
        
        if nums[0] == 0:
            return False
        
        dp = [-1] * n
        dp[0] = nums[0]
        
        
        i = 1
        while i < n:
            dp[i] = max(dp[i - 1], i + nums[i])
            print(i, dp[i])
            if dp[i] >= n - 1:
                return True
            if dp[i] == i:
                return False
            i += 1
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        while i < n:
            if 0 < nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
                temp = nums[i]
                nums[i] = nums[temp - 1]
                nums[temp - 1] = temp
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
            
        return n + 1

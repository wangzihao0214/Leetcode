class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        result = nums[0]
        
        for i in range(1, n):
            result ^= nums[i]
        
        return result
    
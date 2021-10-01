class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        n = len(nums)
        result = 0
        
        left = 0
        product = 1
        for right in range(n):
            product *= nums[right]
            
            while product >= k:
                product /= nums[left]
                left += 1
            
            result += right - left + 1
        
        return result
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        
        if n == 0:
            return -1
        
        while True:
            if left > n - 1 or right < 0:
                return -1
            
            mid = left + (right - left + 1) // 2
            
            if target == nums[mid]:
                return mid
            
            if left >= right:
                return -1

            if target > nums[mid]:
                left = mid + 1
                
            if target < nums[mid]:
                right = mid - 1
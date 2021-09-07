class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        
        if n == 0:
            return [-1, -1]
        
        while True:
            if left > n - 1 or right < 0:
                return [-1, -1]
            
            mid = left + (right - left + 1) // 2
            
            if target == nums[mid]:
                break
            
            if left >= right:
                return [-1, -1]

            if target > nums[mid]:
                left = mid + 1
                
            if target < nums[mid]:
                right = mid - 1
        
        left = mid
        right = mid
        while left > 0 and nums[left - 1] == target:
            left -= 1
            
        while right < n - 1 and nums[right + 1] == target:
            right += 1
        
        return [left, right]
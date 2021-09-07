class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] <= nums[i + 1]:
            i += 1
        nums = nums[i + 1:] + nums[:i + 1]
        
        left = 0
        right = n - 1
        len_rotated = n - i - 1
        
        if n == 0:
            return -1
        
        while True:
            if left > n - 1 or right < 0:
                return -1
            
            mid = left + (right - left + 1) // 2
            
            if target == nums[mid]:
                if mid < len_rotated:
                    mid = mid + n - len_rotated
                else:
                    mid = mid - len_rotated
                return mid
            
            if left >= right:
                return -1

            if target > nums[mid]:
                left = mid + 1
                
            if target < nums[mid]:
                right = mid - 1
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def get(i):
            if i == -1 or i == n:
                return float('-inf')
            return nums[i]
        
        n = len(nums)
        
        left = 0
        right = n - 1
        
        while True:
            if left == right:
                return left
            
            mid = (left + right) // 2
            
            if get(mid - 1) < get(mid) > get(mid + 1):
                return mid
            
            if get(mid) < get(mid + 1):
                left = mid + 1
            else:
                right = mid
        
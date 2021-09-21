class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1
        
        while True:
            print(left, right)
            if left == right:
                return nums[left]
            
            mid = (left + right) // 2
            if nums[left] > nums[mid]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                return nums[left]
        
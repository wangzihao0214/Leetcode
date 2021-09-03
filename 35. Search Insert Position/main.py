class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1

        if n == 0:
            return 0

        while True:
            if left > n - 1:
                return n

            if right < 0:
                return 0

            mid = left + (right - left + 1) // 2

            if target == nums[mid]:
                return mid

            if left >= right:
                if target > nums[left]:
                    return left + 1
                else:
                    return left

            if target > nums[mid]:
                left = mid + 1

            if target < nums[mid]:
                right = mid - 1
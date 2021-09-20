class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1

        while True:
            if left > right:
                return [-1, -1]
            if nums[left] != target or nums[right] != target:
                if nums[left] != target:
                    left += 1
                if nums[right] != target:
                    right -= 1
            else:
                return [left, right]

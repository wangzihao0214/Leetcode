def threeSum(nums):
    class Solution:
        def threeSum(self, nums: List[int]) -> List[List[int]]:
            nums = sorted(nums)
            n = len(nums)
            result = []

            i = 0
            while i <= n - 3:
                left = i + 1
                right = n - 1

                while left != right:
                    if nums[i] + nums[left] + nums[right] > 0:
                        right -= 1
                    elif nums[i] + nums[left] + nums[right] < 0:
                        left += 1
                    elif nums[i] + nums[left] + nums[right] == 0:
                        result.append([nums[i], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left - 1] == nums[left]:
                            left += 1

                i += 1
                while i <= n - 3 and nums[i - 1] == nums[i]:
                    i += 1

            return result

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        left = 0
        right = 0
        s = 0
        result = n
        larger = False

        for right in range(n):
            s += nums[right]

            if s < target:
                right += 1
            else:
                larger = True
                while s >= target:
                    length = right - left + 1
                    if length < result:
                        result = length
                    s -= nums[left]
                    left += 1

        if larger:
            return result
        else:
            return 0

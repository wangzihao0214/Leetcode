class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        times = 0
        pointer = 0
        while times < n:
            if nums[pointer] == 0:
                    nums[:] = nums[: pointer] + nums[pointer + 1:] + [0]
            else:
                pointer += 1
            times += 1
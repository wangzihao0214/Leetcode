class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # n = len(nums)
        # for i in range(k):
        #     nums.insert(0, nums[-1])
        #     nums.pop()
        
        n = len(nums)
        k = k % n
        
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        
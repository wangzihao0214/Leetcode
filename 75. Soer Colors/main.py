class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        bucket0 = []
        bucket1 = []
        bucket2 = []
        
        for i in range(n):
            if nums[i] == 0:
                bucket0.append(0)
            elif nums[i] == 1:
                bucket1.append(1)
            else:
                bucket2.append(2)
        
        nums[:] = bucket0 + bucket1 + bucket2
        
#         n = len(nums)
        
#         pivot = 1
#         while pivot < n:
#             temp = pivot
#             index = temp - 1
#             while temp > 0 :
#                 index = temp - 1
#                 if nums[index] > nums[temp]:
#                     if index == 0:
#                         nums[:] = [nums[temp]] + [nums[0]] + nums[2:]
#                     else:
#                         nums[:] = nums[: index] + [nums[temp]] + [nums[index]] + nums[temp + 1:]
#                     temp -= 1
#                 else:
#                     break
#             pivot += 1
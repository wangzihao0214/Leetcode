class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
    
#         n = len(nums)
#         dic = {}
#         result = 1
        
#         if len(nums) == 0:
#             return 0
        
#         for i in range(n):
#             dic[nums[i]] = 1
#             if nums[i] + 1 in dic.keys():
#                 dic[nums[i]] = dic[nums[i] + 1] + 1
#                 if dic[nums[i]] > result:
#                     result = dic[nums[i]]
#             cur = nums[i] - 1
#             while cur in dic.keys():
#                 dic[cur] = dic[cur + 1] + 1
#                 if dic[cur] > result:
#                     result = dic[cur]
#                 cur -= 1
        
#         return result

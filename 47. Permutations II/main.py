class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [[] for _ in range(n)]
        
        result[0].append([nums[0]])
        for i in range(1, n):
            for ele in result[i - 1]:
                for j in range(len(ele) + 1):
                    temp = ele[:j] + [nums[i]] + ele[j:]
                    if temp not in result[i]:
                        result[i].append(temp)
                    
        return result[n - 1]
            
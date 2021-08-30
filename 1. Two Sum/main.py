class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, ele in enumerate(nums):
            dic[ele] = i
        for i, ele in enumerate(nums):
            num2 = target - ele
            if dic.get(num2):
                j = dic[num2]
                if dic[num2] != i:
                    return [i, j]

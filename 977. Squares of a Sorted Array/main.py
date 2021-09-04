class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums_negative = []
        nums_positive = []
        result = []
        
        for i in range(n):
            if nums[i] < 0:
                nums_negative.append(nums[i])
            else:
                nums_positive.append(nums[i])
        nums_negative = nums_negative[::-1]
        
        n1 = len(nums_negative)
        n2 = len(nums_positive)
        for i in range(n1):
            nums_negative[i] = nums_negative[i]**2
        for i in range(n2):
            nums_positive[i] = nums_positive[i]**2
            
        pointer1 = 0
        pointer2 = 0
        while pointer1 < n1 and pointer2 < n2:
            if nums_negative[pointer1] < nums_positive[pointer2]:
                result.append(nums_negative[pointer1])
                pointer1 += 1
            else:
                result.append(nums_positive[pointer2])
                pointer2 += 1
        if pointer1 == n1:
            result += nums_positive[pointer2: n2]
        if pointer2 == n2:
            result += nums_negative[pointer1: n1]
        
        return result
    
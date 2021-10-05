class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0
        if nums[0] >= n - 1:
            return 1
        
        
        result = 1
        cur = 0
        farthest = nums[cur]
        while farthest < n - 1:
            print(cur, farthest)
            for i in range(farthest, cur, -1):
                temp = i + nums[i]
                if temp > farthest:
                    farthest = temp
                    cur = i
            result += 1
        return result
    
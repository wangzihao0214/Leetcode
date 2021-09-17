class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrace(path, k, start_index):
            if k == 0:
                result_k.append(path[:])
                return
            for i in range(start_index, n):
                path.append(nums[i])
                backtrace(path, k - 1, i + 1)
                path.pop()
        
        
        n = len(nums)
        result = []
        for k in range(n + 1):
            result_k = []
            path = []
            backtrace(path, k, 0)
            result += result_k
        
        return result
        
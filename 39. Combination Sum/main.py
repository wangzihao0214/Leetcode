class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(path, s, start_index):
            if s == 0:
                self.result.append(path[:])
                return
            if s < 0:
                return
            for i in range(start_index, n):
                path.append(candidates[i])
                backtrace(path, s - candidates[i], i)
                path.pop()
        
        n = len(candidates)
        self.result = []
        
        backtrace([], target, 0)
        return self.result
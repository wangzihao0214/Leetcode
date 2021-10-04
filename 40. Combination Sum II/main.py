class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrace(path, s, start_index):
            if s == 0:
                if path not in self.result:
                    self.result.append(path[:])
                return
            if s < 0:
                return
            temp = -1
            for i in range(start_index, n):
                if candidates[i] != temp: # 剪枝
                    path.append(candidates[i])
                    backtrace(path, s - candidates[i], i + 1)
                    temp = path.pop()
        
        n = len(candidates)
        candidates = sorted(candidates)
        self.result = []
        
        if sum(candidates) < target:
            return []
        
        backtrace([], target, 0)
        return self.result
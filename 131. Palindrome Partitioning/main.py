class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def pal(s):
            return s == s[::-1]
        def backtrace(path, start_index):
            if start_index == n:
                self.result.append(path[:])
                return
            for i in range(start_index, n):
                if pal(s[start_index: i + 1]):
                    path.append(s[start_index: i + 1])
                    backtrace(path, i + 1)
                    path.pop()
        
        n = len(s)
        self.result = []
        backtrace([], 0)
        return self.result
                
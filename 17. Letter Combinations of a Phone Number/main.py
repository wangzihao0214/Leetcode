class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def backtrace(path, cur):
            if len(path) == n:
                self.result.append("".join(path))
                return
            for c in mapping[digits[cur]]:
                path.append(c)
                backtrace(path, cur + 1)
                path.pop()

        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        n = len(digits)
        if n == 0:
            return None
        self.result = []
        backtrace([], 0)
        return self.result
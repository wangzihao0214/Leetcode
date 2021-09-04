class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {"2": "abc", "3":"def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        n = len(digits)
        
        if n == 0:
            return []
        
        length = 1
        for i in range(n):
            length *= len(mapping[digits[i]])
        result = [""] * length
        
        for i in range(n):
            repeat = 1
            for j in range(i + 1, n):
                repeat *= len(mapping[digits[j]])
            
            pointer = 0
            times = 0
            for k in range(length):
                result[k] += mapping[digits[i]][pointer]
                times += 1
                if times == repeat:
                    pointer += 1
                    pointer = pointer % len(mapping[digits[i]])
                    times = 0
            
        return result
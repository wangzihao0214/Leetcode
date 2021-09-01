class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = len(s)
        zigzag = [[] for i in range(numRows)]
        result = []
        row = 0
        flag = 1
        
        if numRows == 1:
            return s
        
        for i in range(n):
            zigzag[row].append(s[i])
            if row == 0:
                flag = 1
            if row == numRows - 1:
                flag = -1
            row += flag
            
        for i in range(numRows):
            result += zigzag[i]
        return "".join(result)
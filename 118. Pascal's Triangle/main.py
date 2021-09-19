class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[] for _ in range(numRows)]
        
        result[0].append(1)
        
        for i in range(1, numRows):
            result[i].append(1)
            for j in range(1, i):
                result[i].append(result[i - 1][j - 1] + result[i - 1][j])
            result[i].append(1)
        
        return result

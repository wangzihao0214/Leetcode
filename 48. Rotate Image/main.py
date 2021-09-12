class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        x_center = (n - 1) / 2
        
        i = 0
        while i < x_center:
            length = n - i * 2
            for j in range(i, i + length - 1):
                temp1 = matrix[i][j]
                k = 0
                while k < 4:
                    temp2 = matrix[j][n - 1 - i]
                    matrix[j][n - 1 - i] = temp1
                    temp1 = temp2
                    i, j = j, n - 1 - i
                    k += 1
            i += 1
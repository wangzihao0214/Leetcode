class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        left = 0
        right = n - 1
        row = -1
        
        for i in range(m):
            if matrix[i][left] <= target <= matrix[i][right]:
                row = i
                break
        
        if row == -1:
            return False
        
        while True:
            if left > right:
                return False
            
            mid = (left + right) // 2
            
            if matrix[row][mid] == target:
                return True
            if matrix[row][mid] > target:
                right = mid - 1
            if matrix[row][mid] < target:
                left = mid + 1

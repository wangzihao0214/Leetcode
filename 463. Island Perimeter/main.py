class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        result = 0
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if i == 0:
                        result += 1
                    if i == row - 1:
                        result += 1
                    if j == 0:
                        result += 1
                    if j == col - 1:
                        result += 1
                    for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        i_new = i + direction[0]
                        j_new = j + direction[1]
                        if 0 <= i_new < row and 0 <= j_new < col:
                            if grid[i_new][j_new] == 0:
                                result += 1
        
        return result
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dic_row = [{} for _ in range(9)]
        dic_col = [{} for _ in range(9)]
        dic_box = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    box = (i // 3) * 3 + j // 3
                    
                    dic_row[i][num] = dic_row[i].get(num, 0) + 1
                    dic_col[j][num] = dic_col[j].get(num, 0) + 1
                    dic_box[box][num] = dic_box[box].get(num, 0) + 1
                    
                    if dic_row[i][num] > 1 or dic_col[j][num] > 1 or dic_box[box][num] > 1:
                        return False
                    
        return True
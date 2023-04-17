class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    for num in range(1,10):
                        if self.isValid(board, row, col, str(num)):
                            board[row][col] = str(num)
                            if self.solveSudoku(board):
                                return True
                            else:
                                board[row][col] = "."
                    return False
        return True

        
    def isValid(self, board, row, col, num):
        for i in range(9):
            if board[row][i] == num:
                return False
            
        for i in range(9):
            if board[i][col] == num:
                return False
        
        start_row = row - row%3
        start_col = col - col%3
        
        for i in range(3):
            for j in range(3):
                if board[start_row+i][start_col+j] == num:
                    return False
        
        return True
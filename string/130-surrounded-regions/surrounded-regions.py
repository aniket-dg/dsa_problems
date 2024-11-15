class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        def capture(i,j):
            if i < 0 or i > ROWS-1 or j < 0 or j > COLS-1 or board[i][j] != "O":
                return 
            board[i][j] = "T"
            capture(i+1, j)
            capture(i-1, j)
            capture(i, j+1)
            capture(i, j-1)

        for i in range(ROWS):
            for j in range(COLS):
                if (i in (0, ROWS-1) or j in (0, COLS-1)) and board[i][j] == "O":
                    capture(i, j)

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "T":
                    board[i][j] = "O"
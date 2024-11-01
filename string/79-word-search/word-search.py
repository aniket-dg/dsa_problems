class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # word_remaining = word
        rows, cols = len(board), len(board[0])
        indexes = []
        paths = set()
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    indexes.append((row, col))
                    
        def dummy(i, j, word_remaining):
            # print(i, j, word_remaining)
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False

            if not word_remaining:
                return True
                
            if (i, j) in paths:
                return False

            if board[i][j] != word_remaining[0]:
                return False

            if board[i][j] == word_remaining[0] and not word_remaining[1:]:
                return True
                
            paths.add((i, j))

            res =  (dummy(i+1, j, word_remaining[1:]) or
                    dummy(i-1, j, word_remaining[1:]) or
                    dummy(i, j+1, word_remaining[1:]) or
                    dummy(i, j-1, word_remaining[1:])
                )   
            paths.remove((i, j))
            return res
            
        # print(indexes)
        for row, col in indexes:
            if dummy(row, col, word):
                return True
        return False
class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        mat = [["0" for _ in range(n)] for _ in range(m)]
        for row, col in guards:
            mat[row][col] = "G"

        for row, col in walls:
            mat[row][col] = "W"

        directions = {  # name : [row, col]
                        "up": [-1, 0],
                        "down": [1, 0],
                        "left": [0, -1],
                        "right": [0, 1]
                    }

        def dfs(row, col, direction):
            if row not in range(0, m) or col not in range(0, n) or mat[row][col] == "W" or mat[row][col] == "G":
                return 

            mat[row][col] = "X"

            dfs(row + directions[direction][0], col + directions[direction][1], direction)

        for row, col in guards:
            dfs(row-1, col, "up")
            dfs(row+1, col, "down")
            dfs(row, col-1, "left")
            dfs(row, col+1, "right")

        count = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == "0":
                    count += 1

        return count
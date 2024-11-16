class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            if row == len(triangle):
                return 0
            left, right = dfs(row + 1, col), dfs(row + 1, col+1)
            memo[(row, col)] = min([triangle[row][col] + left, triangle[row][col] + right])
            return memo[(row, col)]
        return dfs(0, 0)
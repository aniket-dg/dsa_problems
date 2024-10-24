class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        matrix = obstacleGrid
        m, n = len(matrix), len(matrix[0])
    
        memo = [[-1]*n for _ in range(m)]
        
        def dfs(i, j):
            if i >= m or j>=n or matrix[i][j] == 1:
                return 0 
            
            if i == m-1 and j == n-1:
                return 1 
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            right = dfs(i, j+1)
            down = dfs(i+1, j)
            
            memo[i][j] = right + down 
            return memo[i][j]
        if matrix[0][0] == 1 or matrix[m-1][n-1] == 1:
            return 0
        return dfs(0,0)
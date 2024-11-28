class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        dq = deque([(0, 0, 0)]) # row, col, obstacles_removed
        visited = [[False]*cols for _ in range(rows)]
        visited[0][0] = True
        while dq:
            row, col, obstacles_removed = dq.popleft()
            if row == rows-1 and col == cols-1:
                return obstacles_removed

            for dx, dy in directions:
                r = row + dx
                c = col + dy

                if 0 <= r < rows and 0 <= c < cols and not visited[r][c]:
                    visited[r][c] = True
                    if grid[r][c] == 1:
                        dq.append((r, c, 1 + obstacles_removed))
                    else:
                        dq.appendleft((r, c, obstacles_removed))
        
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        directions = [[1,0], [0,1], [-1, 0], [0, -1]]
        pq = [(0,0,0)]
        visited = [[False]*cols for _ in range(rows)]
        # visited[0][0] = True

        while pq:
            time, r, c = heapq.heappop(pq)
            if r == rows-1 and c == cols-1:
                return time

            if visited[r][c]:
                continue
            visited[r][c] = True
            for dx, dy in directions:
                new_r = r + dx
                new_c = c + dy
                if 0 <= new_r < rows and 0 <= new_c < cols:
                    td = (grid[new_r][new_c] - time) % 2 == 0
                    new_t = max(time + 1, td + grid[new_r][new_c])
                    heapq.heappush(pq, (new_t, new_r, new_c))
        return -1
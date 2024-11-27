class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i+1] for i in range(n)]

        def dfs():
            q = deque()
            q.append((0, 0))
            visited = set()
            visited.add((0,0))
            while q:
                curr, length = q.popleft()
                if curr == n-1:
                    return length

                for nei in adj[curr]:
                    if nei not in visited:
                        q.append((nei, length+1))
                        visited.add(nei)

        res = []
        for n1, n2  in queries:
            adj[n1].append(n2)
            res.append(dfs())

        return res
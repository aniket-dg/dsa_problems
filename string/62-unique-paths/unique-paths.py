class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = 0
        memo = {}
        def dummy(start, end):
            print(start, end)
            if (start, end) in memo:
                return memo[(start, end)]
            if start >= m or end >= n:
                memo[(start, end)] = 0
                return memo[(start, end)]
                
            if start == m-1 and end == n-1:
                memo[(start, end)] =  1
                return memo[(start, end)]

            memo[(start, end)] = dummy(start+1, end) + dummy(start, end+1)
            return memo[(start, end)]

        res = dummy(0, 0)
        return res
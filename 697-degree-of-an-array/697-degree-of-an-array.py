class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        memo = {}
        degree = 0
        visited = {}
        res = float('inf')
        for i, item in enumerate(nums):
            if item not in visited:
                visited[item] = i
            memo[item] = memo.get(item, 0) + 1
            if memo[item] > degree:
                degree = memo[item]
                res = i - visited[item] + 1
            elif memo[item] == degree:
                res = min(res, i-visited[item]+1)
        return res
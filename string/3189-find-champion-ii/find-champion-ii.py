class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        memo = [0]*n

        for strong, weak in edges:
            memo[weak] += 1

        res = -1
        count = 0
        for i, item in enumerate(memo):
            if item == 0:
                count += 1
                res = i

        return res if count == 1 else -1
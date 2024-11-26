class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        memo = {}
        for i, row in enumerate(mat):
            memo[i] = row.count(1)
        return [item[0] for item in sorted(memo.items(), key=lambda item: (item[1], item[0]))[:k]]
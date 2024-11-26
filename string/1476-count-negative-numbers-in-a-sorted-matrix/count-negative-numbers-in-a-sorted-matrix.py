class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg_count = 0
        for row in grid:
            for item in row:
                if item < 0:
                    neg_count += 1
        return neg_count
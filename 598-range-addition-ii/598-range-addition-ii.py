class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        minRow, minCol = m, n
        for op in ops:
            minRow = min(minRow, op[0])
            minCol = min(minCol, op[1])            
        return minRow * minCol
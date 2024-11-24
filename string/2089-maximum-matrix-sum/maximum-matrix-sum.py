class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_min = float("inf")
        negative_count = 0
        total = 0
        rows, cols = len(matrix), len(matrix[0])
        
        for row in range(rows):
            for col in range(cols):
                num = matrix[row][col]
                if num < 0:
                    negative_count += 1
                abs_min = min(abs_min, abs(num))
                total += abs(num)

        return total if negative_count % 2 == 0 else total - (2*abs_min) 
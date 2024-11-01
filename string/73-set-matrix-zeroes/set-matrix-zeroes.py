class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nums = matrix
        rows, cols = len(nums), len(nums[0])
        rowZero = False

        for row in range(rows):
            for col in range(cols):
                if nums[row][col] == 0:
                    nums[0][col] = 0

                    if row > 0:
                        nums[row][0] = 0
                    else:
                        rowZero = True

        for row in range(1, rows):
            for col in range(1, cols):
                if nums[0][col] == 0 or nums[row][0]==0:
                    nums[row][col] = 0

        if nums[0][0] == 0:
            for row in range(rows):
                nums[row][0] = 0

        if rowZero:
            for col in range(cols):
                nums[0][col] = 0

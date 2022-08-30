class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m,n = len(matrix), len(matrix[0])
        res = [[0 for i in range(len(matrix))] for j in range(len(matrix[0]))]

        for i in range(0, len(matrix[0])):
            for j in range(0, len(matrix)):
                res[i][j] = matrix[j][i]
        return res
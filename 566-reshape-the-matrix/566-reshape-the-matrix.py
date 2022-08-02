class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        memo = [[i for i in range(c)] for j in range(r)]
        res = []
        mat_row = len(mat)
        mat_col = len(mat[0])
        if not mat_row*mat_col == r*c:
            return mat
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                 res.append(mat[i][j])
    #     return res

        counter = 0
        for row in range(len(memo)):
            for col in range(len(memo[0])):
                print(counter)
                memo[row][col] = res[counter]
                counter += 1
        return memo
class Solution:
    def edit(self, a, b, i, j, memo):
        if i == len(a):
            return len(b)-j
        if j == len(b):
            return len(a)-i
        if memo[i][j] != -1:
            return memo[i][j]
        ans = 0
        if a[i] == b[j]:
            return self.edit(a, b, i+1, j+1, memo)
        else:
            insert_ans = 1 + self.edit(a, b, i, j+1, memo)
            delete_ans = 1 + self.edit(a, b, i+1, j, memo)
            replace_ans = 1 + self.edit(a, b, i+1, j+1, memo)
            ans = min(insert_ans, delete_ans, replace_ans)
        memo[i][j] = ans
        return memo[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        memo = [[-1 for i in range(len(word2))] for j in range(len(word1))]
        return self.edit(word1, word2, 0, 0, memo)
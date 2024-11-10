class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = float("-inf")
        idx = -1
        for i in range(len(mat)):
            a = Counter(mat[i])
            if a[1] > count:
                count = a[1]
                idx = i
        return [idx, count]
class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res = [0]*32
        for n in candidates:
            i = 0
            while n > 0:
                res[i]+= n&1
                n = n >> 1
                i += 1
        return max(res)
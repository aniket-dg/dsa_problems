class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        from collections import Counter
        a = Counter(nums)
        res = 0
        for i, v in a.items():
            if v == 1:
                res += i
        
        return res
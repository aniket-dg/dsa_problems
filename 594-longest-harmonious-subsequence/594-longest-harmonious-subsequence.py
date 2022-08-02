class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        a = list(set(nums))
        a.sort()
        for i in range(1, len(a)):
            if a[i] - a[i-1] == 1:
                first = nums.index(a[i-1])
                last = len(nums) - nums[::-1].index(a[i])-1
                res = max(res, last-first+1)
        return res
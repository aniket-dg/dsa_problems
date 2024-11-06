class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        i = 0
        while i < len(nums):
            res.append(nums[i])
            j = i + 1
            while j < len(nums):
                print(nums[j], end="")
                here = res[-1] + nums[j]
                res.append(here)
                j += 1
            print()
            i += 1
        # print(sorted(res)[left-1:right])
        return sum(sorted(res)[left-1:right])%(10**9+7)
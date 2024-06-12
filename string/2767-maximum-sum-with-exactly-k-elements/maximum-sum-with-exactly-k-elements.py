class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        n = 0
        res = 0
        while n < k:
            max_digit = max(nums)
            idx = nums.index(max_digit)
            nums.pop(idx)
            nums.append(max_digit+1)

            res += max_digit
            n += 1
        return res
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums)==0:
            return 0
        nums.sort()
        i = 1
        res = float("-inf")
        count = 1
        while i < len(nums):
            # print(nums[i], nums[i-1], count, res)
            if nums[i]-1 == nums[i-1]:
                count += 1
            else:
                res = max(res, count)
                count = 1
            i += 1
        res = max(res, count)
        return res
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        res = nums.index(max(nums))
        nums.sort()
        if nums[-2]*2 <= nums[-1]:
            return res
        return -1
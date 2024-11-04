class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        idx_to_remove = []
        res = []
        while i < len(nums):
            current = nums[i]
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i += 1
                res.append(i)
            
            idx_to_remove += res[1:].copy()
            res = []
            i += 1

        for item in idx_to_remove[::-1]:
            nums.pop(item)
        return len(nums)
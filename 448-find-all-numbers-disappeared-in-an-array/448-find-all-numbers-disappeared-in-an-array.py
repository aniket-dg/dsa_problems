class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for item in nums:
            i = abs(item) - 1
            nums[i] = -1 * abs(nums[i])
        
        res = []
        for i, val in enumerate(nums):
            if val > 0:
                res.append(i+1)
        return res
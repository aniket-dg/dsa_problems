class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        
        for i, item in enumerate(nums):
            right -= item
            if left == right:
                return i
            left += item
        
        return -1
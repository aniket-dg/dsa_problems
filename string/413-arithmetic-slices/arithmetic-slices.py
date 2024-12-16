class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        total = 0
        for i in range(0, len(nums)-1):
            diff = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == diff:
                    total += 1
                else:
                    break
        return total
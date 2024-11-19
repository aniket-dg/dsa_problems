class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def old_rob(nums):
            rob1, rob2 = 0,0
            for n in nums:
                temp = max(n + rob1, rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        return max(old_rob(nums[1:]), old_rob(nums[:-1]))
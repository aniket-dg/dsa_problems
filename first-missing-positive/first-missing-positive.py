class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        memo = {}
        for i in range(len(nums)):
            memo[nums[i]] = 1
        
        for i in range(1, len(nums)+1):
            if i not in memo:
                return i
        
        return i+1
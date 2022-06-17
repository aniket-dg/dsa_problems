class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memo= {}
        for i, item in enumerate(nums):
            res = target - item
            if res in memo:
                return [memo[res], i]
            memo[item] = i
            
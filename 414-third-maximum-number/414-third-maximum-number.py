class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # nums = list(set(nums))
        # nums.sort()
        # return nums[-3] if len(nums)>=3 else max(nums)
        memo = [float('-inf'),float('-inf'),float('-inf')]
        for item in nums:
            if item not in memo:
                if item > memo[0]:
                    memo = [item, memo[0], memo[1]]
                elif item > memo[1]:
                    memo = [memo[0], item, memo[1]]
                elif item > memo[2]:
                    memo = [memo[0], memo[1], item]
        return max(nums) if float('-inf') in memo else memo[2]
    
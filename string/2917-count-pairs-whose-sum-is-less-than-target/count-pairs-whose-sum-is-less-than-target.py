class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        res = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i < j < len(nums) and nums[i] + nums[j] < target:
                    res.add((i, j))
        return len(res)
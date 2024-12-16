class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_num = min(nums)
            idx = nums.index(min_num)
            nums.pop(idx)
            nums.insert(idx, min_num*multiplier)
        return nums
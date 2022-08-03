class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, k-1
        res = float('-inf')
        count = sum(nums[i:j+1])
        while j<len(nums):
            res = max(count/k, res)
            i += 1
            j += 1
            if j < len(nums):
                count = count - nums[i-1] + nums[j]
        return res
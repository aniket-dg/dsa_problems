class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        def get_len(nums):
            if nums[0] %2 != 0 or nums[0] > threshold:
                return 0
            
            for i in range(1, len(nums)):
                if nums[i]%2 == nums[i-1]%2 or nums[i] > threshold:
                    return 0
            return len(nums)
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                res = max(get_len(nums[i: j+1]), res)
        return res
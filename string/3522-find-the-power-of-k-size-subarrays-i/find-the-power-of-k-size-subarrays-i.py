class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        def is_strictly_increasing(nums):
            for i in range(len(nums) - 1):
                if nums[i]+1 != nums[i + 1]:
                    return -1
            return nums[-1]
            
        res = []
        for i in range(0, len(nums)):
            if len(nums)-i>=k:
                print(nums[i:i+k])
                res.append(is_strictly_increasing(nums[i:i+k]))
        return res
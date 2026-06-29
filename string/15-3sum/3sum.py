class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num = nums[i]
            j, k = i + 1, len(nums)-1
            while j < k:
                sum_here = nums[j] + nums[k]
                if sum_here == 0 - num:
                    res.append([num, nums[j], nums[k]])
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    k -= 1
                    j += 1
                elif sum_here > 0 - num:
                    k -= 1
                else:
                    j += 1
        return res
                    
        
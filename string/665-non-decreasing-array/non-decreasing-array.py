class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # count = 0
        # for i in range(len(nums)-1):
        #     if nums[i]>nums[i+1]:
        #         count +=1
        #     if count >= 2:
        #         break
        # return count < 2
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if count == 1:
                    return False
                count += 1
                if i >= 2 and nums[i-2] > nums[i]:
                    nums[i] = nums[i-1]
        return True
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i,item in enumerate(nums):
            if item!= val:
                nums[k] = nums[i]
                k += 1
        return k
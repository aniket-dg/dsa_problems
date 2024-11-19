class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = l + (r-l)//2
            left = float("-inf") if mid==0 else nums[mid-1]
            right = float("-inf") if mid == len(nums) - 1 else nums[mid+1]
            if left < nums[mid] > right:
                return mid
            elif nums[mid] < right:
                l = mid + 1
            else:
                r = mid - 1
        return -1
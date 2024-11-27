class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)
        while l <= r:
            mid = l + (r-l+1)//2
            greater_than_mid = len(nums) - bisect_left(nums, mid)
            print(mid, greater_than_mid)
            if greater_than_mid == mid:
                return mid
            elif greater_than_mid < mid:
                r = mid - 1
            else:
                l = mid + 1
        return -1
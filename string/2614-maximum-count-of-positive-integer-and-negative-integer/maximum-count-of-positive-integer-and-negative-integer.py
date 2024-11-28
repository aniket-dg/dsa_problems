class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        def search(nums, k):
            l, r = 0, len(nums)-1
            res = -1
            while l <= r:
                mid = l + (r-l+1)//2
                if nums[mid] <= k:
                    l = mid + 1
                    res = mid
                else:
                    r = mid - 1

            return res
        last_neg_index = search(nums, -1)
        last_zero_index = search(nums, 0)
        till_zero_count = last_zero_index + 1
        neg_count = last_neg_index + 1

        pos_count = len(nums) - till_zero_count

        return max(neg_count, pos_count)
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            nums1 = nums[i:i+k]
            nums2 = nums[i+k:i+k*2]
            print(nums1, nums2)
            if len(set(nums1)) == len(set(nums2)) == k and sorted(nums1)==nums1 and sorted(nums2)==nums2:
                return True
        return False
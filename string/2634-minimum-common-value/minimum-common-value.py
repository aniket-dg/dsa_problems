class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
        # def search(nums, k):
        #     l, r = 0, len(nums)-1
        #     while l <= r:
        #         mid = l + (r-l+1)//2
        #         if nums[mid]==k:
        #             return True
        #         elif nums[mid] < k: 
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return False
        
        # if len(nums2) < len(nums1):
        #     nums1, nums2 = nums2, nums1 

        # for item in nums1:
        #     if search(nums2, item):
        #         return item
        # return -1
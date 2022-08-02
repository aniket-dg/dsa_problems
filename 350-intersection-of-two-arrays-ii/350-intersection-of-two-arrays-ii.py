class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1, nums2 = min(nums1, nums2, key=len), max(nums1, nums2, key=len)
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        res = []
        for item in nums1:
            if item in nums2:
                res.append(item)
                nums2.remove(item)
        return res
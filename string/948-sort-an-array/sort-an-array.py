class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums_here):
            if len(nums_here) > 1:
                mid = len(nums_here)//2
                left = nums_here[:mid]
                right = nums_here[mid:]
                merge(left)
                merge(right)

                i = j = k = 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        nums_here[k] = left[i]
                        i += 1
                    else:
                        nums_here[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    nums_here[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    nums_here[k] = right[j]
                    j += 1
                    k += 1
                
            return nums
        return merge(nums)
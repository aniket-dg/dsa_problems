class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start, end):
            while start <= end:
                mid = start + end-1 //2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    return binary_search(start, mid-1)
                else:
                    return binary_search(mid+1, end)
                
            return -1
        
        return  binary_search(0, len(nums)-1)
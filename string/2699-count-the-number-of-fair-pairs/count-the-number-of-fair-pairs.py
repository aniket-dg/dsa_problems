class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def get_index(nums, target,start, smallest=True):
            low, high = start, len(nums)-1
            res = -1
            while low <= high:
                mid = low + (high-low)//2
                if smallest:
                    if nums[mid]>=target:
                        res = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                else:
                    if nums[mid]<=target:
                        res = mid
                        low = mid + 1
                    else:
                        high = mid - 1
            return res

        nums.sort()
        res = 0
        for i in range(len(nums)-1):
            item = nums[i]
            lower_bound = lower - item
            upper_bound = upper - item

            
            first_index, last_index = get_index(nums, lower_bound,i+1, True) , get_index(nums, upper_bound,i+1, False)
            if first_index != -1 and last_index != -1 and first_index <= last_index:
                res += last_index-first_index + 1
        return res
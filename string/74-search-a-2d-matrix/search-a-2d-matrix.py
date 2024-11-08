class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix)-1
        while low < high:
            mid = low + (high-low)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                if matrix[mid][-1] <= target:
                    low = mid
                    break
                else:
                    high = mid
            else:
                if matrix[mid][-1] >= target:
                    low = mid
                    break
                low = mid + 1

        nums = matrix[low]
        low, high = 0, len(nums)
        while low < high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return False

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def search(row):
            l, r = 0, len(row)-1
            while l <= r:
                mid = l + (r-l+1)//2
                if row[mid]>=0:
                    l = mid + 1
                else:
                    r = mid - 1
            return l

        prev = None
        res = 0
        for row in grid:
            if prev and prev >= 0:
                res += len(row)
                continue
            first_negative_index = len(row) - search(row)
            res += first_negative_index
        return res
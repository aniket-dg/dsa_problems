class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def can_work(item):
            need_store = 0
            for quantity in quantities:
                need_store += (quantity-1)//item +1
                if need_store > n:
                    return False
            return True
        low, high = 1, max(quantities)
        res = -1
        while low <= high:
            mid = low + (high-low)//2
            if can_work(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return res
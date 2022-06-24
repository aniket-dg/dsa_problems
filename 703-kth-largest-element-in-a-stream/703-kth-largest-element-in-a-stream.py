class KthLargest:
    res = []
    k = None
    def __init__(self, k: int, nums: List[int]):
        self.res = nums
        self.res.sort()
        self.k = k

    def add(self, val: int) -> int:
        self.res.append(val)
        self.res.sort()
        return self.res[-self.k]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
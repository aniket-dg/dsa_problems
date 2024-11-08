class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        kmax = (1<<maximumBit) - 1
        xorr = 0
        res = [0]*n
        for i in range(n):
            xorr ^= nums[i]
            res[n-i-1] = xorr^kmax
        return res
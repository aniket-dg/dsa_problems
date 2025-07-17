class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        memo = {}
        for i, item in enumerate(nums):
            if item in memo and abs(memo[item] - i) <= k:
                return True
            memo[item] = i
        
        return False

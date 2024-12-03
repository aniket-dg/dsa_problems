class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        counter = Counter(nums)
        for num, count in counter.items():
            if count > 2:
                return False
        return True
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxFar = 0
        maxHere = 0
        for item in nums:
            if item:
                maxHere += 1
            else:
                maxFar = max(maxFar, maxHere)
                maxHere = 0
        maxFar = max(maxFar, maxHere)
        return maxFar
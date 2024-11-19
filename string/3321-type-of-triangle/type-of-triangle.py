class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if not sum(nums[:2]) > nums[-1]:
            return "none"
        sides = set(nums)
        types = ["equilateral","isosceles", "scalene"]
        return types[len(sides)-1]
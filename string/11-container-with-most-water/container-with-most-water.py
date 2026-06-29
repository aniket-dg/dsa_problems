class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxAreaRes = float("-inf")
        while l <= r:
            length = r - l
            width = min(height[l], height[r])
            area = length * width
            maxAreaRes = max(maxAreaRes, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxAreaRes    
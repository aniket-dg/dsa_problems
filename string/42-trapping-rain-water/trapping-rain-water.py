class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxLeft, maxRight = 0, 0
        water = 0
        while l < r:
            maxLeft = max(maxLeft, height[l])
            maxRight = max(maxRight, height[r])
            if height[l] < height[r]:
                l += 1
                water += max(0, maxLeft - height[l])
            else:
                r -= 1
                water += max(0, maxRight - height[r])
        return water
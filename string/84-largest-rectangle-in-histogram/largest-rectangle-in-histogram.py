class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_height = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                max_height = max(max_height, h * (i-index))
                start = index

            stack.append((start, height))

        while stack:
            index, h = stack.pop()
            max_height = max(max_height, h * (len(heights)-index))
        return max_height
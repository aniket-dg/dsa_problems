class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            stack = []
            max_height = 0
            for i, height in enumerate(heights):
                start = i
                while stack and stack[-1][1] > height:
                    index, h = stack.pop()
                    max_height = max(max_height, int(h) * (i-index))
                    start = index

                stack.append((start, height))

            while stack:
                index, h = stack.pop()
                max_height = max(max_height, int(h) * (len(heights)-index))
            return max_height
        
        max_height = 0
        res = [0]*len(matrix[0])
        for row in matrix:
            for j in range(len(row)):
                res[j] = res[j] + int(row[j]) if int(row[j]) else int(row[j])
            max_height = max(max_height, largestRectangleArea(res))        
        return max_height
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        max_num = 0
        for i, item in enumerate(arr):
            if item >= max_num:
                max_num = item
            if max_num == i:
                chunks += 1
        return chunks
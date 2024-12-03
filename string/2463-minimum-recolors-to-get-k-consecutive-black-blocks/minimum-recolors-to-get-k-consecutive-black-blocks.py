class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = len(blocks)
        for i in range(len(blocks)-k+1):
            block_here = blocks[i: i+k]
            res = min(res, block_here.count("W"))
        return res
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        memo = []
        start = end = 0
        memo = [int(i) for i,data in enumerate(s) if data == c]
        res = []
        for i, item in enumerate(s):
            a = min(memo, key=lambda x: abs(x-i))
            res.append(abs(a-i))
        return res  
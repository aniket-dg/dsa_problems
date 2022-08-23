class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        n = 1
        byt = 0
        for c in s:
            curr = widths[ord(c)-ord('a')]
            if curr + byt > 100:
                n += 1
                byt = curr
            else:
                byt += curr
        return n, byt   
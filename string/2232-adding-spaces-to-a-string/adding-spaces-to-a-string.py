class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = ""
        prev = 0
        for space in spaces:
            here = s[prev: space]
            prev = space
            res += here
            res += " "
        res += s[prev:]

        return res
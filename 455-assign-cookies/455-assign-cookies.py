class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        i = j = 0
        counter = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                counter += 1
                j += 1
                i += 1
            elif s[j] < g[i]:
                j += 1
        return counter
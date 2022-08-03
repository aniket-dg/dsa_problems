class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        window = {}
        needN = len(countT)
        haveN = 0
        res, resLen = [-1, -1], float('inf')
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                haveN += 1
            while haveN == needN:
                if (r-l+1) < resLen:
                    res = [l, r]
                    resLen = (r-l+1)
                # last = s[l]
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    haveN -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""
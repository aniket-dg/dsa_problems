class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        minStr = min(strs)
        for i in range(len(minStr)):
            currS = minStr[i]
            for item in strs:
                if item[i] != currS:
                    return res
            res += currS
        return res
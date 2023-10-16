class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        memo = set()

        for i in range(len(s)):
            while s[i] in memo:
                memo.remove(s[l])
                l += 1
            memo.add(s[i])
            res = max(res, i-l+1)
        
        return res
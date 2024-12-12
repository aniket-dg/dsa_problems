class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        memo = defaultdict(int)
        i = 0
        memo[s[0]] += 1
        memo[s[1]] += 1
        res = 2
        for j in range(2, len(s)):
            char = s[j]
            while memo[char] >= 2:
                memo[s[i]] -= 1
                i += 1
            memo[char] += 1
            res = max(res, j-i+1)
        return res
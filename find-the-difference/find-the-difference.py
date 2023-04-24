class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) < len(t):
            s,t = t,s
        
        memo = Counter(t)

        for item in s:
            if item not in memo or memo[item] < 1:
                return item
            else:
                memo[item] -= 1
        
        return -1
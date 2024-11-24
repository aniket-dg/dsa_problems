class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        memo = {}
        for i in range(0, len(s)):
            str_here = s[i: i+10]
            if len(str_here) == 10:
                if str_here in memo:
                    res.add(str_here)
                else:
                    memo[str_here] = 1
            else:
                break
        return list(res)
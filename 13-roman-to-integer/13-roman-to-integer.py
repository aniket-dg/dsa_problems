class Solution:
    def romanToInt(self, s: str) -> int:
        memo = {
        'I':1,"V": 5, "X": 10, "L":50, "C":100, "D": 500, "M": 1000
        }
        if len(s)==1:
            if s[0] in memo:
                return memo[s[0]]
            return
        # print(s)
        currE = memo.get(s[0])
        nextE = memo.get(s[1])

        if nextE > currE:
            sumHere = nextE - currE
            if len(s) > 2:
                return sumHere + self.romanToInt(s[2:])
            return sumHere
        else:
            sumHere = currE
            if len(s)>1:
                return sumHere + self.romanToInt(s[1:])
            return sumHere
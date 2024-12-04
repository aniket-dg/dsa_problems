class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = ""
        stop = 0
        for i in range(0, len(s)-2*k, 2*k):
            stop = i+2*k
            str_here = s[i: i+2*k]
            rev_str = str_here[:k][::-1]
            normal_str = str_here[k:]
            # print(rev_str + normal_str)
            res += rev_str + normal_str
        
        if stop != len(s):
            # print(s[stop:stop+k][::-1] + s[stop+k:])
            res += s[stop:stop+k][::-1] + s[stop+k:]
        return res
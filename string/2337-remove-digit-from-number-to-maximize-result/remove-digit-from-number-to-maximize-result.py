class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        a = number
        res = float("-inf")

        for i, number in enumerate(a):
            if number == str(digit):
                build = a[:i] + a[i+1:]
                res = max(res, int(build))

        return str(res)
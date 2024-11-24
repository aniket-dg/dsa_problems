class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)
        integer_part =  numerator//denominator
        remainder = numerator%denominator
        res.append(str(integer_part))
        if remainder == 0:
            return "".join(res)
            
        memo = {}
        res.append(".")
        while remainder:
            if remainder in memo:
                res.insert(memo[remainder], "(")
                res.append(")")
                break

            memo[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder//denominator))
            remainder %= denominator

        return "".join(res)
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = twenty = 0
        for item in bills:
            if item == 5:
                five += 1
            elif item == 10:
                ten += 1
                five -= 1
            else:
                if ten > 0:
                    ten -= 1
                    five -= 1
                else:
                    five -= 3
            if five < 0:
                return False
        if five < 0:
            return False
        return True 
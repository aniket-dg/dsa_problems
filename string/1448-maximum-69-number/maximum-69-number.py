class Solution:
    def maximum69Number (self, num: int) -> int:
        maxNum = max(float('-inf'), num)
        i = 0
        num = str(num)
        while i < len(num):
            digit = int(num[i])
            if digit == 6:
                new_digit = num[:i] + "9" + num[i+1:]
            else:
                new_digit = num[:i] + "6" + num[i+1:]

            maxNum = max(int(new_digit), maxNum)
            i += 1
        return maxNum
        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_num = 0
        n = x
        while n>0:
            new_num = new_num *10 + n%10
            n = n//10
        return new_num == x
        # return x == 
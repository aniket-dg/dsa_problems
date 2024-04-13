class Solution:
    def minimumSum(self, num: int) -> int:
        a = list(map(int,sorted(str(num))))
        total = int(str(a[0])+str(a[-1])),  int(str(a[1])+str(a[2]))
        return sum(total)
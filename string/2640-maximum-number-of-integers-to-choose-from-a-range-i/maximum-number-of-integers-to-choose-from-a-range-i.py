class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        eligible = [i for i in range(1, n+1) if i not in banned]
        count = 0
        total = 0
        res = []
        for item in eligible:
            if count+1 <= n and total+item <= maxSum:
                count += 1
                total += item
                res.append(item)
            else:
                break
        return count
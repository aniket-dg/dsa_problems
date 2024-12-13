class Solution:
    def findScore(self, nums: List[int]) -> int:
        res = []
        score = 0
        data = sorted([[item, i] for i, item in enumerate(nums)], key=lambda x:[x[0], x[1]])
        seen = set()
        for num, index in data:
            if index in seen:
                continue
            seen.add(index)
            score += num
            if index-1>=0:
                seen.add(index-1)
            if index+1<len(nums):
                seen.add(index+1)
        return score
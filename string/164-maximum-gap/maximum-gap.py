class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        low, high = min(nums), max(nums)
        buckets = defaultdict(list)

        for num in nums:
            if num == high:
                index = n-1
            else:
                index = abs(num-low)*(n-1)//(high-low)

            buckets[index].append(num)

        existing_bucket = []
        for i in range(n):
            if buckets[i]:
                existing_bucket.append([min(buckets[i]), max(buckets[i])])

        res = 0
        for i in range(1, len(existing_bucket)):
            res = max(res, abs(existing_bucket[i-1][-1] - existing_bucket[i][0]))
        return res
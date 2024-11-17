class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = float("inf")
        curr_sum = 0
        min_heap = []

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum >= k:
                res = min(res, i+1)

            while min_heap and curr_sum - min_heap[0][0] >= k:
                prefix, index = heapq.heappop(min_heap)
                res = min(res, i - index)

            heapq.heappush(min_heap, (curr_sum, i))

        return res if res != float("inf") else -1
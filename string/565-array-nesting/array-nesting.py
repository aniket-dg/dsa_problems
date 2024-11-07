class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        # i = 0
        # res = []
        # while i < len(nums):
        #     j = nums[i]
        #     k = j
        #     res_here = [j]
        #     while j != i:
        #         j = nums[j]
        #         res_here.append(j)
        #     res.append(len(res_here))
        #     i += 1
        # return max(res)
        n = len(nums)
        res = 0
        visited = [False]*n

        for num in nums:
            count = 0
            while not visited[num]:
                count += 1
                visited[num] = True
                num = nums[num]
            res = max(res, count)
        return res
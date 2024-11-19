class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        start = 0
        n = len(nums)
        unique_elements = set()
        curr_sum = 0
        for end in range(n):
            if nums[end] not in unique_elements:
                curr_sum += nums[end]
                unique_elements.add(nums[end])

                if end - start + 1 == k:
                    if max_sum < curr_sum:
                        max_sum = curr_sum

                    curr_sum -= nums[start]
                    unique_elements.remove(nums[start])
                    start += 1
            else:
                while nums[start] != nums[end]:
                    curr_sum -= nums[start]
                    unique_elements.remove(nums[start])
                    start += 1
                start += 1
        return max_sum
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        from collections import Counter, defaultdict
        if nums == sorted(nums):
            return True
        bin_nums = []
        memo = defaultdict(int)
        for item in nums:
            bin_value = bin(item).replace("0b", "")
            bin_nums.append(bin_value)
            memo[item] = Counter(bin_value)

        for _ in range(len(nums)):
            for i in range(len(nums)-1):
                num1_setbits = memo.get(nums[i])["1"]
                num2_setbits = memo.get(nums[i+1])["1"]
                if nums[i] > nums[i+1] and num1_setbits == num2_setbits:
                    nums[i],nums[i+1] = nums[i+1], nums[i]

        return nums == sorted(nums)
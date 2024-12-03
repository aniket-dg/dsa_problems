class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        res = 0
        nums = str(num)
        for i in range(len(nums)-k+1):
            print(nums[i:i+k])
            num_here = int(nums[i:i+k])
            if num_here > 0 and num%int(nums[i:i+k]) == 0:
                res += 1
        return res
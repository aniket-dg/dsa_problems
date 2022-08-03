class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        postfix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1]+nums[i])
        for i in range(len(nums)-2, -1, -1):
            postfix.append(postfix[-1] + nums[i])
        
        postfix = postfix[::-1]
        
        for i in range(len(prefix)):
            if prefix[i] == postfix[i]:
                return i
        return -1
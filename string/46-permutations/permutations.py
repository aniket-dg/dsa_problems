class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(nums)):
            if len(nums)==1:
                return [nums[:]]
                
            n = nums.pop(0)
            perms = self.permute(nums)
            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
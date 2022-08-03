class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        memo = [0]
        for item in nums:
            memo.append(memo[-1]+item)
        
        ans = float('-inf')
        for i in range(len(nums)-k+1):
            ans = max(memo[i+k]-memo[i], ans)
        return ans/float(k)
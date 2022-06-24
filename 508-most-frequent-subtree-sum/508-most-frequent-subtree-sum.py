# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {}
    max_sum = 0
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root):
            if not root:
                return 0
            
            sum_here = root.val + dfs(root.left) + dfs(root.right)
            if sum_here in self.memo:
                self.memo[sum_here] += 1
            else:
                self.memo[sum_here] = 1
            if self.max_sum < self.memo[sum_here]:
                self.max_sum = self.memo[sum_here]
            return sum_here
            
        res = []
        self.memo = {}
        self.max_sum = 0
        dfs(root)
        
        for item in self.memo:
            if self.memo[item] == self.max_sum:
                res.append(item)
        return res
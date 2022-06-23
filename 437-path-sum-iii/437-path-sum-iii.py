# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
      
    
    def dfs(self, root, target):
        if root:
            return int(root.val == target) + self.dfs(root.left, target-root.val) + self.dfs(root.right, target-root.val)
        return 0

    def pathSum(self, root, targetSum):
        sum = targetSum
        if root:
            return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        return 0
    
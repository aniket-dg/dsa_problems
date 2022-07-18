# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    currSum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def dfs(node, val):
            if not node:
                return val
            val = dfs(node.right, val)
            node.val += val
            return dfs(node.left, node.val)
            
        dfs(root, 0)
        return root
    

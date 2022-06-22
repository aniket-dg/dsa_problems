# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_level = 1
        left = root.left
        right_level = 1
        right = root.right
        
        while left:
            left_level += 1
            left = left.left
        
        while right:
            right_level += 1
            right = right.right
        
        if left_level == right_level:
            return  (2**left_level) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
    
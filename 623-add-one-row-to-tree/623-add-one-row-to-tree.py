# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def helper(node, currDepth):
            if not node:
                return 
            if currDepth == depth - 1:
                temp = node.left
                node.left = TreeNode(val)
                node.left.left = temp

                temp = node.right
                node.right = TreeNode(val)
                node.right.right = temp
                return
            
            
            helper(node.left, 1 + currDepth)
            helper(node.right, 1 + currDepth)
                    
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot
        
        else:
            helper(root, 1)
            return root
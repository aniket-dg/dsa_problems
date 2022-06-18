# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    first = None
    mid = None
    last = None
    prev = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.bst(root)
        if self.first and self.last:
            self.first.val, self.last.val = self.last.val, self.first.val
        else:
            self.first.val, self.mid.val = self.mid.val, self.first.val
    
    def bst(self, root):
        if not root:
            return
        
        self.bst(root.left)
        
        if self.prev and root.val < self.prev.val:
            if not self.first:
                self.first = self.prev
                self.mid = root
            
            else:
                self.last = root
        
        self.prev = root
        self.bst(root.right)
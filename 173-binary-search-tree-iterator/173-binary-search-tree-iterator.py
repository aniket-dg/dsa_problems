# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = self.inorder(root)[::-1]

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack)>0
        
    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
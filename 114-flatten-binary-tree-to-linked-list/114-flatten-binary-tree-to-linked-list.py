# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # root_bk = root
        # def preorder(root):
        #     if not root:
        #         return []
        #     return [root.val] + preorder(root.left) + preorder(root.right)
        # nums = preorder(root_bk)
        # j = 1
        # res = root
        # while j < len(nums):
        #     print(nums[j])
        #     res.left = None
        #     res.right = TreeNode(nums[j])
        #     # res.left = TreeNode(None)
        #     res = res.right
        #     j += 1
        
#         Morris Traversal
        # curr = root
        # while curr:
        #     if curr.left:
        #         predecessor = curr.left
        #         while predecessor and predecessor.right:
        #             predecessor = predecessor.right
        #         predecessor.right = curr.right
        #         curr.right = curr.left
        #         curr.left = None
        #     curr = curr.right
        
        def dfs(root):
            if not root:
                return None
            
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            
            if root.left:
                leftTail.right = root.right
                root.right = root.left
                root.left = None
            
            return rightTail or leftTail or root
        dfs(root)
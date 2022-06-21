# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr, res):
            curr += str(root.val)
            if not root.left and not root.right:
                res.append(curr)
            if root.left:
                dfs(root.left, curr, res)

            if root.right:
                dfs(root.right, curr, res)

        if not root:
            return
        res = []
        curr = str(root.val)

        if not root.left and not root.right:
            res.append(curr)

        if root.left:
            dfs(root.left, curr, res)

        if root.right:
            dfs(root.right, curr, res)



        res = sum(list(map(int, res)))
        return res
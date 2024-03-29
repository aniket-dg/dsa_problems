# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         def dfs(root):
#             if not root:
#                 return []
#             return dfs(root.left) + [root.val] + dfs(root.right)
        
#         res = dfs(root)
#         if len(res) > 0:
#             return res[k-1]
#         return 0
        n = 0
        stack = []
        
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right
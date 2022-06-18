# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        memo = {}
        for i, val in enumerate(inorder):
            memo[val] = i
        def dfs(low, high):
            if low > high:
                return None
            root = TreeNode(postorder.pop())
            mid = memo[root.val]
            root.right = dfs(mid+1, high)
            root.left = dfs(low, mid-1)
            return root
        
        return dfs(0, len(inorder)-1)
#         if not inorder or not postorder:
#             return None
#         root = TreeNode(postorder.pop())
#         mid = inorder.index(root.val)
#         root.right = self.buildTree(inorder[mid+1:], postorder)
#         root.left = self.buildTree(inorder[:mid], postorder)
        
#         return root

    

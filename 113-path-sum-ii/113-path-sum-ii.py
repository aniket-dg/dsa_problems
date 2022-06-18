# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = []
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(root, currSum, ele):
            if not root:
                return False
            currSum += root.val
            if not root.left and not root.right:
                if currSum == targetSum:
                    ele += [root.val]
                    self.res.append(ele)
            
            dfs(root.left, currSum, ele + [root.val])
            dfs(root.right, currSum, ele + [root.val])
        self.res = []
        dfs(root, 0, [])
        return self.res
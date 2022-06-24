# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def dfs(root):
            if root:
                res.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        res = []
        dfs(root)
        return " ".join(res)
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        preorder = list(map(int, data.split(" "))) if len(data) > 0 else []
        inorder = sorted(preorder)
        
        def makeTree(preorder, inorder):
            if not preorder and not inorder:
                return None
            
            root = TreeNode(preorder[0])
            mid = inorder.index(root.val)
            
            root.left = makeTree(preorder[1:mid+1], inorder[:mid])
            root.right = makeTree(preorder[mid+1:], inorder[mid+1:])
            
            return root
        
        return makeTree(preorder, inorder)
            
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
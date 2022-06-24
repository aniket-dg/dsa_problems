# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        from queue import Queue
        q = Queue()
        q.put(root)
        while not q.empty():
            temp = Queue()
            while not q.empty():
                curr = q.get()
                if curr.right:
                    temp.put(curr.right)

                if curr.left:
                    temp.put(curr.left)
                
            q = temp
        return curr.val
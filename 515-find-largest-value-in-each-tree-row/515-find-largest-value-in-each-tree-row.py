# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        from queue import Queue
        q = Queue()
        q.put(root)
        res = []
        while not q.empty():
            temp = Queue()
            level_node = []
            while not q.empty():
                curr = q.get()
                if curr:
                    level_node.append(curr.val)
                    if curr.left:
                        temp.put(curr.left)
                    if curr.right:
                        temp.put(curr.right)
            
            if level_node:
                res.append(max(level_node))
            level_node = []
            q = temp
        return res
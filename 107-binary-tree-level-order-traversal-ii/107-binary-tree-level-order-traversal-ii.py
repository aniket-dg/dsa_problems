# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue, res = collections.deque([root, 0]), []
        while queue:
            res.append([node.val for node in queue if node])
            queue = [child for node in queue if node for child in (node.left, node.right) if node]
        return res[-2::-1]
#         from queue import Queue
#         if not root:
#             return []
#         q = Queue()
#         q.put(root)
#         res = []
#         while not q.empty():
#             temp = Queue()
#             temp_res = []
#             while not q.empty():
#                 curr = q.get()
#                 temp_res.append(curr.val)
#                 if curr.left:
#                     temp.put(curr.left)
#                 if curr.right:
#                     temp.put(curr.right)
            
#             q = temp
#             res.insert(0, temp_res)
#         return res
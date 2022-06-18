# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from queue import Queue
        if not root:
            return []
        q = Queue()

        q.put(root)
        rev = False
        res = []
        while not q.empty():
            temp = Queue()
            temp_res = []
            while not q.empty():
                curr = q.get()
                if curr.left:
                    temp.put(curr.left)
                if curr.right:
                    temp.put(curr.right)
                temp_res.append(curr.val)
            if rev:
                res.append(temp_res[::-1])
                rev = not rev
            else:
                res.append(temp_res)
                rev = not rev
            q = temp
        return res
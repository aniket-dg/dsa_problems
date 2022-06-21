"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        from queue import Queue
        q = Queue()
        q.put(root)
        
        while not q.empty():
            size = q.qsize()
            dummy = Node(0)
            while size:
                node = q.get()
                dummy.next = node
                dummy = dummy.next
                
                if node.left:
                    q.put(node.left)
                
                if node.right:
                    q.put(node.right)
                
                size -= 1
        
        return root
                    
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def generate(head):
            if not head:
                return None
            
            mid = getmid(head)
            root = TreeNode(mid.val)
            if mid.val == head.val:
                return root
            root.left = generate(head)
            root.right = generate(mid.next)
            
            return root
        
        def getmid(head):
            prev = slow = fast = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            if prev:
                prev.next = None
            
            return slow
        
        return generate(head)
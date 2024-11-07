# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode()
        start = prev
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
            else:    
                prev.next = head
                prev = head
                head = head.next
            
            if start is None:
                start = prev
        while head:
            prev.next = head
            prev = head
            head = head.next
        prev.next = None
        return start.next
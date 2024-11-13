# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        prev = ListNode(-1)
        old_start = prev
        new_start = ListNode()
        smaller = new_start
        while head:
            if head.val < x:
                smaller.next = head
                prev.next = head.next
                smaller = smaller.next
            else:
                prev.next= head
                prev = head
                
            head = head.next

        prev.next = None
        smaller.next = old_start.next if old_start.next is not None else (prev if prev.val != -1 else None)
        # printNode(new_start.next)
        return new_start.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_nodes(head):
            prev = None
            curr = head
        
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            return prev, head
        left_most = right_most = left_node = right_node = None
        prev = None
        start = head
        position = 1
        while head:
            if position == left:
                left_node = head
                left_most = prev
                if left_most:
                    left_most.next= None
            if position == right:
                right_node = head
                right_most = head.next
                right_node.next = None
                break
            prev = head
            head = head.next
            position += 1

        if not left_node:
            return start
        
        new_left, new_right = reverse_nodes(left_node)
        if left_most:
            left_most.next = new_left
        else:
            start = new_left
        new_right.next = right_most
        return start
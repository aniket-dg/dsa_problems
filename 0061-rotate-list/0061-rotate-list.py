# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        start = head
        n = 0
        while head:
            n += 1
            
            prev = head
            head = head.next

        # print(prev.val, "last_end", prev.next, start.val)
        prev.next = start
        res = prev
        # print(prev.val, "prev")
        old_head = start
        res = prev
        new_head = old_head
        i = 1
        calculated_k = k % n if k % n != 0 else n
        calculated_k = n - calculated_k
        # print(calculated_k, "calculated_k", n, "n", k, "k")
        if calculated_k > 0:
            while i < calculated_k:
                new_head = new_head.next
                i += 1
            res = new_head.next
            new_head.next = None
        else:
            prev.next = None
            res = old_head


        return res
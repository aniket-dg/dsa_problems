# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        x = self.head
        reservoir = x.val
        count = 1
        while x.next:
            x = x.next
            count += 1
            if random.randint(1, count) == 1:
                reservoir = x.val
        return reservoir


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
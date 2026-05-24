# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next is None or head is None:
            return False
        curr = head
        fast_curr = head
        while curr:
            if curr == fast_curr:
                return True
            curr = curr.next
            fast_curr = fast_curr.next.next
        return False
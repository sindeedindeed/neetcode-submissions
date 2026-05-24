# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        if head.next is None:
            return False
        curr = head
        fast_curr = head
        while curr:
            curr = curr.next
            fast_curr = fast_curr.next.next
            if curr == fast_curr:
                return True
        return False
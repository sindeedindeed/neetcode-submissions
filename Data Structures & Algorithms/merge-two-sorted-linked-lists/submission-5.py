# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        if curr1 is None and curr2 is None:
            return None
        if curr2 is None:
            return curr1
        if curr1 is None:
            return curr2

        head = curr1 if curr1.val > curr2.val else curr2
        curr = head

        while curr1.next and curr2.next:
            next1 = curr1.next
            next2 = curr2.next
            if curr1.val >= curr2.val:
                curr.next = curr2
                curr1 = next1 
            else:
                curr.next = curr1
                curr2 = next2
        
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        curr1 = list1
        curr2 = list2
        if curr1.next is None:
            curr1.next = curr2
            return curr1
        if curr2.next is None:
            curr2.next = curr1
            return curr2
        while curr1.next or curr2.next:
            if curr1.next:
                next1 = curr1.next
            if curr2.next:
                next2 = curr2.next
            if curr1.val <= curr2.val:
                curr1.next = curr2
                curr1 = next1
            if curr2.val <= curr1.val:
                curr2.next = curr1
                curr2 = next2
        

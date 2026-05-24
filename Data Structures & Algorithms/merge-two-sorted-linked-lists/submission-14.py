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
        if curr1.val <= curr2.val: curr3 = curr1
        else: curr3 = curr2
        head3 = curr3
        while curr1.next and curr2.next:
            if curr1.val <= curr2.val:
                curr3 = curr1
                curr1 = curr1.next
            else:
                curr3 = curr2
                curr2 = curr2.next
            curr3 = curr3.next

        return head3
                
        

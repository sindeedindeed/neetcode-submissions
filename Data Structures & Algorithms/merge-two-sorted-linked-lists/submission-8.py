# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        curr3 = None

        while curr1.next and curr2.next:
            if curr1.val > curr2.val:
                curr3 = curr1
                curr1 = curr1.next
            else:
                curr3 = curr2
                curr2 = curr2.next
        
        return curr3

        


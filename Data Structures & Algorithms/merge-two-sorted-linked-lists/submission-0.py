# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ls: ListNode
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            ls = list1
            list1 = list1.next
        else:
            ls = list2
            list2 = list2.next
        head = ls

        while list1 is not None and list2 is not None:
            
            if list1.val < list2.val:
                ls.next = list1
                list1 = list1.next
            else:
                ls.next = list2
                list2 = list2.next
            
            ls = ls.next
        if list1 is not None:
            ls.next = list1
        elif list2 is not None:
            ls.next = list2

        return head
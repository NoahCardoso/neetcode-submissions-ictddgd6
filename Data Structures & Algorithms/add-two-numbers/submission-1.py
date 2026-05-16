# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number = ListNode()
        head = number
        overflow = 0
        while l1 != None and l2 != None:
            c = l1.val + l2.val + overflow
            print(c)
            if c > 9:
                overflow = 1
                c = c%10
            else:
                overflow = 0
            number.val = c
            l1 = l1.next
            l2 = l2.next
            if l1 != None and l2 != None:
                number.next = ListNode()
                number = number.next
        if number.val != None and (l1 != None or l2 != None):
            number.next = ListNode()
            number = number.next
        while l1 != None:
            
            c = l1.val + overflow
            
            if c > 9:
                overflow = 1
                c = c%10
            else:
                overflow = 0
            number.val = c
            l1 = l1.next
            if l1 != None:
                number.next = ListNode()
                number = number.next
            
        while l2 != None:
            c = l2.val + overflow
            if c > 9:
                overflow = 1
                c = c%10
            else:
                overflow = 0
            number.val = c
            
            l2 = l2.next
            if l2 != None:
                number.next = ListNode()
                number = number.next
        if overflow != 0:
            number.next = ListNode()
            number = number.next
            number.val = overflow
        
        return head

        
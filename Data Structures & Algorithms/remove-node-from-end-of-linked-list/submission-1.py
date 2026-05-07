# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = head
        p = None
        
        size = 0
        curr = head
        while curr != None:
            curr = curr.next
            size += 1
        #if size == n and size == 1: return None
        for _ in range(size-n):
            
            p = c
            
            c = c.next
        
        if c == None:
            p.next = None
        elif p == None:
            return head.next
        else:
            p.next = c.next
        
        return head
        
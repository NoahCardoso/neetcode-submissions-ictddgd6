# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            stack = []
            curr = prev_group.next

            for _ in range(k):
                if not curr:
                    return dummy.next
                stack.append(curr)
                curr = curr.next

            while stack:
                prev_group.next = stack.pop()
                prev_group = prev_group.next

            prev_group.next = curr
            
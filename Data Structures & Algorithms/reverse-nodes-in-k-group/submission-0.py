# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        while group_prev:
            group_end = group_prev
            ctr = 0
            while group_end and ctr < k:
                group_end = group_end.next
                ctr += 1
            if not group_end:
                break
            group_next = group_end.next
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            first_in_group = group_prev.next
            group_prev.next = group_end
            group_prev = first_in_group

        return dummy.next
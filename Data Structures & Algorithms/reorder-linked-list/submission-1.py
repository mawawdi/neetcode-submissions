# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        slow = fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while second is not None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        while prev is not None:
            temp1 = head.next
            temp2 = prev.next
            head.next = prev
            prev.next = temp1
            prev = temp2
            head = temp1
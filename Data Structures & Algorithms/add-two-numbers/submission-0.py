# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        carry = 0

        while l1 and l2:
            sum = l1.val + l2.val
            with_carry = sum + carry
            carry = with_carry // 10
            sum = with_carry % 10
            node = ListNode(sum)
            curr.next = node
            curr = node
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                sum = l1.val
                with_carry = sum + carry
                carry = with_carry // 10
                sum = with_carry % 10
                node = ListNode(sum)
                curr.next = node
                curr = node
                l1 = l1.next
        else:
            while l2:
                sum = l2.val
                with_carry = sum + carry
                carry = with_carry // 10
                sum = with_carry % 10
                node = ListNode(sum)
                curr.next = node
                curr = node
                l2 = l2.next

        if carry:
            node = ListNode(carry)
            curr.next = node
            curr = node
        
        return head.next
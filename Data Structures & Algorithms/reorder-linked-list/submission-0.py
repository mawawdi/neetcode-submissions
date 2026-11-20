# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        stack = []
        tail = head
        while tail is not None:
            stack.append(tail)
            tail = tail.next
        
        tail = head
        n = len(stack)
        
        for _ in range(n // 2):
            node = stack.pop()
            temp = tail.next
            tail.next = node
            node.next = temp
            tail = temp
        
        tail.next = None
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # """ use stack"""
        # stack = []
        # while head != None:
        #     stack.append(head)
        #     head = head.next
        
        # reverse = stack.pop()
        # tail = reverse

        # while stack:
        #     curr = stack.pop()
        #     tail.next = curr
        #     tail = curr
        
        # return reverse

        """ iterate """
        prev = None
        tail = prev
        while head != None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        return prev






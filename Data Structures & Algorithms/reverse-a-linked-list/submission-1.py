# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        temp = head  
        stack = []   
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        new_list = ListNode(val=stack.pop())
        temp = new_list
        while stack:
            temp.next = ListNode(val=stack.pop())
            temp = temp.next        
        
        return new_list  

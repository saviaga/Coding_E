# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        prev = None
        curr = head
        
        while curr!=None:
            next_n = curr.next
            curr.next = prev
            prev = curr
            curr = next_n
        head = prev
        
        return head
        
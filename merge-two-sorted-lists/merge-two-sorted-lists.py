# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        prehead = ListNode(-1)
        curr = prehead
        
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                l2 = l2.next                
            else:
                curr.next = l1
                l1 = l1.next
            curr = curr.next
        if l1 is not None:
            curr.next = l1 
        else:
            curr.next = l2     
        return prehead.next
        
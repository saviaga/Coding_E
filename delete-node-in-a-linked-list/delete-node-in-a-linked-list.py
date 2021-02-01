# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        #copy the value of next node in the node given
        # 4->1->1->9
        #then point our node.next to node.next.next
        
        node.val = node.next.val
        node.next = node.next.next
        
        
        
        
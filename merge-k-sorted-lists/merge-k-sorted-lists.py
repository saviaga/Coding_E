# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        #We build a min heap with all the list heads that are not null and we store both the value and the node.
        
        h = []
        for a in lists:
            while a is not None:
                heapq.heappush(h, a.val)
                a = a.next
        if not h:
            return None
        

        v0 = heapq.heappop(h)
        head = ListNode(v0)
        prev = head
        while h:
            v = heapq.heappop(h)
            prev.next = ListNode(v)
            prev = prev.next

        return head            
        
                
                
           
        
        
        
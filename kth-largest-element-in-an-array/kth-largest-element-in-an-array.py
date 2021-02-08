class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        heap = []
        i=1
        for value in nums:
            heapq.heappush(heap,-value)
        while i<k:
            heapq.heappop(heap)
            i+=1
            
        
        return -heappop(heap)
        
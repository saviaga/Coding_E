class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        
        i = m-1
        j = n-1
        end = len(nums1)-1
        
        while i>=0 and j>=0:
            if nums1[i] > nums2[j]:
                nums1[end]=nums1[i]
                i-=1
            else:
                nums1[end]=nums2[j]
                j-=1
            end-=1
        
        
        #while still elemens in nums2 copy the rest of the elements that remain in nums2
        while j >= 0:
            nums1[end] = nums2[j]
            j-=1
            end-=1
        return nums1
                
        
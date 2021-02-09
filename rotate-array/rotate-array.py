class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        new_a = [0]*len(nums)
        for i in range(len(nums)):
            np = (i+k)%len(nums)
            
            new_a[np] = nums[i]
            
        nums[:]=new_a
        return nums     
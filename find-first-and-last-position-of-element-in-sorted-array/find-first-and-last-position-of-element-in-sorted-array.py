class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        position = [-1,-1]
        
        for i in range(len(nums)):
            if nums[i]==target:
                position[0] =i
                break
        
                
        for i in reversed(range(len(nums))):
            if nums[i]==target:
                position[1] =i
                break
            
        return position
        
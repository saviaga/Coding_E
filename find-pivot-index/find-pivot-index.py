class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        to_the_left=[0]*(len(nums))
        to_the_right=[0]*(len(nums))
        
        
        #calculate to_the_right values
        for i in range(1,len(nums)):
            to_the_left[i]= to_the_left[i-1]+nums[i-1]
        
        #calculate to_the_left values
        for i in reversed(range(len(nums)-1)):
            to_the_right[i]=to_the_right[i+1]+nums[i+1]
                            
        #find index in which both values are equal
        for i in range(len(nums)):
            if to_the_left[i]==to_the_right[i]:
                return i
        return -1
        #return index
        
                         
        
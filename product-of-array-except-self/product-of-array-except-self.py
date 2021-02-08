class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums)==0:
            return []
        
        new_array = [0]*len(nums)
        to_the_right = [0]*len(nums)
        to_the_left = [0]*len(nums)
        
        to_the_right[0]=1
        to_the_left[len(nums)-1]=1
        
        #fill left_to_right

            
        #fill right_to_left
        for i in reversed(range(len(nums)-1)):
            to_the_left[i] = nums[i+1]*to_the_left[i+1]
            
        for i in range(1,len(nums)):
            to_the_right[i] = to_the_right[i-1]*nums[i-1]
        
        for i in range(len(nums)):
            new_array[i] = to_the_right[i]*to_the_left[i]
        return new_array
                    
                    
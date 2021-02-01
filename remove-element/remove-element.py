class Solution:
    
    
    
    def removeElement(self, nums: List[int], val: int) -> int:
        
        
        #While not end of array#
        
        #slot = find next_avaul_ slot (find value = val)
        #replace next value !=val in slot
        #
        start= 0 
        end = len(nums)-1
                    
        while start <= end:
            
            if nums[start] == val:
                
                nums[start], nums[end] = nums[end], nums[start]
                end-=1
            else:
                start+=1
            
        return start
    

            
        
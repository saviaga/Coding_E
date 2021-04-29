class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
   
        non_dup = 0

        for i in range(len(nums)):            
            if nums[non_dup] != nums[i]:            
                nums[non_dup+1]=nums[i]
                non_dup += 1
                
        return non_dup+1

        
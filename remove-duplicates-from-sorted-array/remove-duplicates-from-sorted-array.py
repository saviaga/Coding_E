class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        non_dup = 0
        
        for i in range(1,len(nums)):
            if nums[non_dup]!=nums[i]:
                non_dup +=1
                nums[non_dup] = nums[i]
                
        return non_dup+1
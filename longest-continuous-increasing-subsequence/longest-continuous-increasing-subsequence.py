class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        prev=float("-inf")
        size = 0
        longest = 0
        for num in nums:
            
            if prev < num:
                size+=1
            else:
                size=1
            prev = num
            longest = max(longest,size)
        
        return longest
        
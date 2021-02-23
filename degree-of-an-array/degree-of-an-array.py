class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
      
        left,right,count = {},{},{}
        
        for i in range(len(nums)):
            if nums[i] not in left:
                left[nums[i]] = i
            
            right[nums[i]] = i
            if nums[i] in count:
                count[nums[i]]+=1
            else:
                count[nums[i]]=1
                
            ans = len(nums)
        degree = max(count.values())
        for elem in count:
            if count[elem]==degree:
                ans = min(ans,right[elem]-left[elem]+1)
        return ans

                
                
        
        
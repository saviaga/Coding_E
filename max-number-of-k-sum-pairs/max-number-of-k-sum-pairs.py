class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        
        ops = 0
        dict_arr = {}
        dict_arr = collections.Counter(nums)
       
        for elem in nums:
            complement = k-elem
            if complement in dict_arr and dict_arr[complement]>0 and dict_arr[elem]>0:
                if (complement == elem) and dict_arr[complement] < 2:
                    continue
                
                else:
                
                    dict_arr[elem]-=1
                    dict_arr[complement]-=1
                    ops+=1
                
        return ops 
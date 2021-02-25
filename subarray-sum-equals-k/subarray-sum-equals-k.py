class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dict_elem = {}
        cs = 0
        count = 0
        for i in range(len(nums)):
            cs += nums[i]
            if cs == k:
                count+=1
            if cs - k in dict_elem:
                count+=dict_elem[cs - k]
            dict_elem[cs] = dict_elem.get(cs,0)+1
        return count
            
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_elem = {}
        for i in range(len(nums)):
            curr_elem = nums[i]
            
            if target - curr_elem in dict_elem:
                return [i,dict_elem[target - curr_elem]]
            else:
                dict_elem[curr_elem] = i
        
            
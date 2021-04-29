class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict_complement = {}
        
        for i in range(len(nums)):
            
            complement = target - nums[i]
            if complement not in dict_complement:
                dict_complement[ nums[i]] = i
            else:
                return i, dict_complement[complement]
        
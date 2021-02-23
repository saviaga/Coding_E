class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
 
        for left in range(len(nums)):
            suma = nums[left]
            for right in range(left+1,len(nums)):
                suma+=nums[right]
                if suma == 0 and k == 0: return True
                if k!=0 and suma%k == 0:
                    return True
        return False
                
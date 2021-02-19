import numpy as np
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        def dfs(nums: list[int], n: int, subset_sum: int) -> bool:
         
            if subset_sum == 0: return True
            if n == 0 or subset_sum < 0: return False

            if not np.isnan(memo[n][subset_sum]):
                return memo[n][subset_sum]
            result = dfs(nums, n - 1, subset_sum - nums[n - 1]) or dfs(nums, n - 1, subset_sum)
            #    #// store the result in memo
            memo[n][subset_sum] = result
            return result


        
        total_sum = sum(nums)
        subset_sum = total_sum // 2
        
        cols,rows = (subset_sum+1),(len(nums)+1)
        memo = np.empty(shape=(rows,cols))
        memo.fill(None)
        if total_sum % 2 != 0:
            return False
        
        n = len(nums)
        return dfs((nums), n - 1, subset_sum)
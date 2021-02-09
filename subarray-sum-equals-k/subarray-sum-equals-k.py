class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = {0:1}
        curr_sum = 0
        count=0
        for elem in nums:
            curr_sum+=elem
            
            if (curr_sum - k) in d:
                    count+=d[curr_sum-k]
            if curr_sum  in d:
                d[curr_sum]+=1
            else:
                d[curr_sum]=1
        return count
        
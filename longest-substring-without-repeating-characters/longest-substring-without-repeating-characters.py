class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        dict_char = {}
        max_lenght = 0
        start = 0
        window_size = 0
        for end in range(len(nums)):
            right_num = nums[end]
            if right_num  in dict_char:
                start = max(start,dict_char[right_num]+1)
            dict_char[right_num] = end
            max_lenght = max(max_lenght,end-start+1)

        return max_lenght
                
            
            
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dict_char = {}
        start = 0
        max_lenght = 0
        
        for end in range(len(s)):
            end_char = s[end]
            if end_char in dict_char:
                start = max(start,dict_char[end_char]+1)
            dict_char[end_char] = end
            max_lenght = max(max_lenght,end-start+1)
        return max_lenght
        
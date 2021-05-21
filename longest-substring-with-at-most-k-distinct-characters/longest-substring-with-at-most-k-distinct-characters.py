class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_lenght = 0
        start = 0
        dict_chars = {}
        
        for end in range(len(s)):
            end_char = s[end]
            if end_char not in dict_chars:
                dict_chars[end_char] = 0
            dict_chars[end_char] +=1
            
            while len(dict_chars) > k:
                start_char = s[start]
                dict_chars[start_char]-=1
                if dict_chars[start_char] ==0:
                    del dict_chars[start_char]
                start+=1
            max_lenght= max(max_lenght,end-start+1)
        return max_lenght
        
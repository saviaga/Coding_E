class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        start = 0
        window_lenght = 0
        window_chars = {}
        max_lenght = 0
        
        
        for end in range(len(s)):
            end_char = s[end]
            
            if end_char not in window_chars:
                window_chars[end_char] = 0
            window_chars[end_char] +=1
            
            #shrink the window
            while len(window_chars) > k:
                start_char = s[start]
                window_chars[start_char] -=1
                if window_chars[start_char] ==0:
                    del window_chars[start_char]
                start+=1
                                
            max_lenght = max(max_lenght,end - start + 1)
        return max_lenght
            
        
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        start,max_repeat,max_length = 0,0,0
        frequency_map = {}
        # Try to extend the window
        for end in range(len(s)):
            right_char = s[end]
            if right_char not in frequency_map:
                frequency_map[right_char] = 0
            frequency_map[right_char] +=1
            #count the max repeating character
            max_repeat = max(max_repeat, frequency_map[right_char])
            
            #overall we have a letter which is repeating max_repeat times
            #we keep advancing and if at some point there are
            #more than k characters end - start + 1 - max_repeat > k
            #it is the time to shrink the window
            
            if end - start + 1 - max_repeat > k:
                left_char = s[start]
                frequency_map[left_char] -= 1
                start+=1
                
            max_length = max(max_length, end - start + 1)
        return max_length
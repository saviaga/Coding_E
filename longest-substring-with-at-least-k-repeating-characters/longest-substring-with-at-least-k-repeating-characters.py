class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        longest = 0
        
        start,end = 0,0

        #count the frequency of each character
       
        maxUnique = len(collections.Counter(s))
        #delete those that have frecuencies of < k
        
        
        #count frequencies of those that remain and that are together 
        for num in range(1,maxUnique+1):
            start = 0
            dict_chars = {}
            for end in range(len(s)):
                end_char = s[end]
                if end_char not in dict_chars:
                    dict_chars[end_char] =0
                dict_chars[end_char] +=1
                
                while (len(dict_chars))> num:
                    start_char = s[start]
                    dict_chars[start_char]-=1
                    if  dict_chars[start_char]==0:
                        del  dict_chars[start_char]
                    start+=1
                if all(val >= k for ch,val in dict_chars.items()):
                    longest = max(longest,end-start+1)
            
                    
        return longest
    
        
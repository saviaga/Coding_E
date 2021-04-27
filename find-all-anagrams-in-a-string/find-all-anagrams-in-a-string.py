class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        start,matched =0,0
        indices = []
        #create counter with the pattern
        dict_pattern = collections.Counter(p)
        
        #go through the string
        for end in range(len(s)):
            right_char = s[end]
            
            if right_char in dict_pattern:
                dict_pattern[right_char] -=1
                
                if dict_pattern[right_char] ==0:
                    matched +=1
            
            if matched == len(dict_pattern):
                indices.append(start)
                
            if end>=len(p)-1:
                left_char = s[start]
                if left_char in dict_pattern:
                    if dict_pattern[left_char]==0:
                        matched -=1
                    dict_pattern[left_char]+=1
                start+=1
        return indices
                    
                
                
        
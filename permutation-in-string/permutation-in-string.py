class Solution:
    def checkInclusion(self, pattern: str, s1: str) -> bool:
        start = 0
        matched = 0
        #create hashmap from the dictionary
        dict_pattern = collections.Counter(pattern)
        
        #go through the window
        for end in range(len(s1)):
            right_char = s1[end]
            
            #if there is a matching character in pattern
            #decrease the pattern hashmap in the char
            
            if right_char in dict_pattern:
                dict_pattern[right_char] -=1
            
                #increase the matched counter if the dict[char] ==0
                #cause maybe a pattern has the same char twice?
                if dict_pattern[right_char] == 0:
                    matched +=1
                        
            if matched == len(dict_pattern):
                return True
            
            #decrease window
            if end >= len(pattern)-1:
                left_char = s1[start]
                if left_char in dict_pattern:
                    if dict_pattern[left_char] == 0:
                        matched -= 1
                
                    dict_pattern[left_char] +=1
                start+=1
            
        return False
            
       
        
        
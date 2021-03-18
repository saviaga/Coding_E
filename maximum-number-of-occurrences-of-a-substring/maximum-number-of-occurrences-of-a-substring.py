class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
#the substring with the maximum number of occurrences is the substring that has the minimum size allowed.        
        start = 0
        end = minSize
        ocurrences = {}
        
        while end <=len(s):
            substring = s[start:end]
            if substring not in ocurrences:
               
                if len(set(substring))<=maxLetters:
                    ocurrences[substring]=1
            else:
                ocurrences[substring]+=1
                    
            start+=1
            end+=1
        if len(ocurrences) ==0:
            return 0
        else:
            return max(ocurrences.values())
                    
                    
                
        
            
        
        
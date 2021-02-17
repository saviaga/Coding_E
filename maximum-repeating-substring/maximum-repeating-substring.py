class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count=0
        rep=""
        i=1
        
        while len(rep)<=len(sequence):
            rep+=word            
            if rep not in sequence:
                return i-1
            else:
                i=i+1
        
        return 0
 
    
               
                
                 
        
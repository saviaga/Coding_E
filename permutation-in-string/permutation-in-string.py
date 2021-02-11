class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dic_s1 = collections.Counter(s1)        
        start=0
        end=len(s1)-1
        while end < len(s2):
            
            dic_temp =  collections.Counter(list(s2[start:end+1]))
            if dic_s1==dic_temp:
                return True  
            start+=1
            end+=1
                
        return False
            

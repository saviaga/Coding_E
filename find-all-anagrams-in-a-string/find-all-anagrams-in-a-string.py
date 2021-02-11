class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        dict_p = collections.Counter(p)
        
        start = 0
        end = len(p)-1
        
        positions = []
        while end < len(s):
            dict_temp=collections.Counter(s[start:end+1])
            if dict_temp==dict_p:
                positions.append(start)
            start+=1
            end+=1
        return positions
                
                
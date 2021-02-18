class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        
        counter = 0
        balanced = 0
        for elem in s:
            if elem == 'R':
                counter+=1
            elif elem == 'L':
                counter-=1
            if counter == 0:
                balanced +=1
        return balanced
            
                
        
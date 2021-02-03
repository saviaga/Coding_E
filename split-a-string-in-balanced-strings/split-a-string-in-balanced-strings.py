class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        
        
        count_balanced = 0
        letter_R = 0
        for elem in s:
            if elem == 'R':
                letter_R+=1
            elif elem =='L':
                letter_R-=1
            if letter_R ==0:
                count_balanced+=1
        return count_balanced
    
    

                
            
            
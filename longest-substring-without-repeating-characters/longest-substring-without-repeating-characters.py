class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s==' ':
            return 1
        
        longest = 0
        substring = set()
        left,right=0,0
        
        while right<len(s):
            
            #if equal and it is not in the set add it

            while (s[right] in substring):
                    substring.remove(s[left])
                    left +=1
            substring.add(s[right])
            longest = max(longest,right-left+1)
            right+=1

                
        
        return longest
            
        
        #["p,w,w,k,e,w"]
# left         ^ 
#right         ^    
#longest=2
#.         ()
        
       
        
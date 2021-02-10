class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s)<=1:
            return True
        
        
        filter_s = filter(lambda ch: ch.isalnum(), s)
        filter_s = list(filter_s)
        sentence = [ch.lower() for ch in filter_s]
        
        start = 0
        end = len(sentence)-1
        while start <= end:
            if sentence[start]!=sentence[end]:
                    return False
            start+=1
            end-=1
        
        return True
        
        
        
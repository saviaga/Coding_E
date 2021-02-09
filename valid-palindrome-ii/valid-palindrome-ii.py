class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1:
            return True
        
        def isPalindromecheck(sub_s,start,end):            
            while start<end:
                if s[start]!=s[end]:
                    return False
                start+=1
                end-=1
            return True
        
        start = 0
        end = len(s)-1
        while start< end:
            if s[start]!=s[end]:
                #if it is not equal then ask the question
                return isPalindromecheck(s,start+1,end) or isPalindromecheck(s,start,end-1)
            start+=1
            end-=1
        return True
            
        
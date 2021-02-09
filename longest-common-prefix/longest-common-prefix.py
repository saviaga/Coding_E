class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        
        longest = max(strs)
        for i in range(len(strs)-1):
            
            #Compare words strs[i] and strs[i+1]
            w1 = strs[i]
            w2 = strs[i+1]
            print(w1,w2)
            j=0
            prefix = ''
            while j < min(len(w1),len(w2)):
                if  w1[j] == w2[j]:
                    prefix+=w1[j]
                elif  w1[j] != w2[j]:
                    break # no point of keep comparing words
                j+=1
            if len(prefix) < len(longest):
                longest = prefix
        return longest
                    
            
            
        
        
        
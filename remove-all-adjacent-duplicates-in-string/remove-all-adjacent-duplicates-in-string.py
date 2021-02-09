class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if len(S)==0:
            return""
        
        stack = [S[0]]
        
        for i in range(1,len(S)):
            if not stack:
                stack.append(S[i])
            else:
                current = stack.pop()
                if current!=S[i]:
                    stack.append(current)
                    stack.append(S[i])
        return "".join(stack)
        
        
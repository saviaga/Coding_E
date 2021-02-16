class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) <=1:
            return False
        
        
        stack = [s[0]]
        
        for i in range(1,len(s)):
                print(s[i])
                if s[i] == '(' or s[i] == '{' or s[i] == '[':
                    stack.append(s[i])
                else: 
                    if stack:
                        top_elem = stack.pop()
                    else:
                        top_elem = 'x'
                    if s[i] == ')' and top_elem != '(':
                            return False
                    elif s[i] == '}' and top_elem != '{':
                            return False
                    elif s[i] == ']' and top_elem !="[":
                            return False
        if len(stack) > 0:
            return False
        else:
            return True
        
        
                
            
        
            
            
            
        
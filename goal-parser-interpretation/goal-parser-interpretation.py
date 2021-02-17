class Solution:
    def interpret(self, command: str) -> str:
        
        mapping = {'G':'G',
                   '()':'o',
                   '(al)':'al'}
        
        parsed = []
        i=1
        while i <=len(command):
            if command[i-1]=='G':
                parsed.append(mapping['G'])
                
            elif command[i-1]=='(' and command[i]==')':
                parsed.append(mapping['()'])
           
            elif command[i-1]=='(' and command[i]=='a':
                parsed.append(mapping['(al)'])
                
            i+=1
        
        return ''.join(parsed)
            
            
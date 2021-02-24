class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        
        
        w = [0]*len(T)
        stack = []
       
        for i in reversed(range(len(T))):
            while stack and T[i]>=T[stack[-1]]:
                stack.pop()
            
            if stack:
                w[i] = stack[-1]-i
            stack.append(i)
            
        return w
            
        
        
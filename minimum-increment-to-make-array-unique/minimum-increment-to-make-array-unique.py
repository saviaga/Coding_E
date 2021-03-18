class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        
        A.sort()
        counter = 0
        
        for i in range(len(A)-1):
            if A[i]>=A[i+1]:
                
                counter+= A[i] - A[i+1] + 1
                A[i+1] = A[i]+1
        return counter
                
            
        
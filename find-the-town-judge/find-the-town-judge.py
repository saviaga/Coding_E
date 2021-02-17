class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        
        outdegree = [0]*(N+1)
        indegree = [0]*(N+1)
        
        for elem in trust:
            outdegree[elem[0]]+=1
            indegree[elem[1]]+=1
            
        for i in range(1,N+1):
            if outdegree[i]==0 and indegree[i]==N-1:
                return i
        else:
            return -1
            
        
        
        
        
        
            
                
            
        
            
            
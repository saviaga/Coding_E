class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        rows, cols = len(text1), len(text2)
        DP = [[0 for i in range(cols+1)] for j in range(rows+1)] #+1 cause we save the 0s
        for i in range(rows):
            for j in range(cols):
                if(text1[i]==text2[j]):
                    DP[i+1][j+1]=DP[i][j]+1
                else:
                    DP[i+1][j+1] = max(DP[i][j+1],DP[i+1][j])
       
        return (DP[-1][-1])         #returns the last position    
        
           
            
            
            
            
            
        
       
        
        
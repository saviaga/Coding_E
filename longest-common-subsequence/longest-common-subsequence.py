class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        rows, cols =  len(text2),len(text1)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)] #+1 cause we save the 0s#+1 cause we save the 0s
    
        
        for c in range(cols):
            for r in range(rows):
                if text2[r] == text1[c]:
                    dp[r+1][c+1] =  dp[r][c]+1 
                else:
                    dp[r+1][c+1] = max(dp[r][c+1],dp[r+1][c])
        return dp[-1][-1]

        
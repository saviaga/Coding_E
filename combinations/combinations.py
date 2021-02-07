class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        def backtracking(first,chosen):
            if len(chosen)==k:
                return res.append(chosen[:])
            else:
                for i in range(first,n+1):
                    #choose                    
                    chosen.append(i)
                    #explore
                    backtracking(i+1,chosen)
                    #unchose
                    chosen.pop()
            
        res = []
        backtracking(1,[])
        return res
            
        
        
        
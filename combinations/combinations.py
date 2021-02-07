class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        
        def combineHelper(first,chosen):
            
            if len(chosen) == k:
                return res.append(chosen[:])
            
            for i in range(first, n+1):
                #chose
                chosen.append(i)
                #explore
                combineHelper(i+1,chosen)
                #unchose
                chosen.pop()
                
            
            
            
        res = []
        combineHelper(1,[])
        return res
        
        
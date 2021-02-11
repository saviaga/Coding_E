class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        
        def tribhelper(k):
            
        
        
            if k in fibo:
                return fibo[k]
                      
            fibo[k] = tribhelper(k-1) + tribhelper(k-2) + tribhelper(k-3)  
            return fibo[k]

        fibo = {0:0,1:1,2:1}
        return tribhelper(n)
    
    
          
        
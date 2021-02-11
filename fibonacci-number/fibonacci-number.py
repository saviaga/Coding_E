class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        
       
            
        fibo = {0:0,1:1}

        if n not in fibo:          
                fibo[n] = self.fib(n-1) + self.fib(n-2)            
        return fibo[n]
        
        
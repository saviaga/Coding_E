class Solution:
    def fib(self, n: int) -> int:
        
        
        dict_nums = {0:0,1:1}
        
        
        def fibHelper(n):
        
            if n in dict_nums:
                return dict_nums[n]
            
            dict_nums[n] = fibHelper(n-1) + fibHelper(n-2)
            
            return dict_nums[n]
            
        return fibHelper(n)
        
        
        
        
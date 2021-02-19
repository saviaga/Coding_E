class Solution:
    def tribonacci(self, n: int) -> int:
        
        def tribonaccihelper(n):
            
            if n in dict_nums:
                return dict_nums[n]
            
            dict_nums[n] = tribonaccihelper(n-1) + tribonaccihelper(n-2) + tribonaccihelper(n-3)
            return dict_nums[n]
            
        dict_nums = {0:0,1:1,2:1}
        return tribonaccihelper(n)
        
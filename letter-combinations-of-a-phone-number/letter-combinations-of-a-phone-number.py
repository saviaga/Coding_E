class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        def backtrack(current,remaining):
        
               
            if len(remaining)==0:
                res.append(current)
            else:
                for c in phone[remaining[0]]:
                   
                    backtrack(current+c,remaining[1:])
        res = []
        phone = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']}
  
        if digits:
            backtrack("",digits)
        return  res
        
        
        

        
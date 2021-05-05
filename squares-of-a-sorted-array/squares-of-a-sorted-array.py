class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squares = [0]*len(nums)
        pt = len(squares)-1
        start = 0
        end = len(squares)-1
        
        
        while start <= end:
            sq_start = nums[start]**2
            sq_end = nums[end]**2
            if sq_start <= sq_end:
                squares[pt] = sq_end
                end-=1
            else:
                squares[pt] = sq_start
                start+=1
            pt-=1
            
        return squares
        
    
        
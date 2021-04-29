class Solution:
    def sortedSquares(self, arr: List[int]) -> List[int]:
        squares = [0]*len(arr)
        highest_index = len(arr)-1
          # TODO: Write your code here
        left = 0
        right = len(arr)-1
        while left <= right:
            sq1 = arr[left]**2
            sq2 = arr[right]**2
            if sq1 > sq2:
                squares[highest_index] = sq1
                left+=1
            else:
                squares[highest_index] = sq2
                right-=1
            highest_index -=1
        return squares
        
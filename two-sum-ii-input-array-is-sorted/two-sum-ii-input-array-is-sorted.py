class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binarySearch(l, r, target):
            while l <= r:
                m = (l + r)//2
                if numbers[m] == target:
                    return m
                elif numbers[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        
        for i in range(len(numbers)):
            curr_elem = numbers[i]
            complement = target - curr_elem
            found = binarySearch(i+1,len(numbers)-1,complement)
            if found != -1:
                return [i+1,found+1]
        
    
        
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        
        
        def is_celebrity(celebrity):
            for person in range(n):
                if person!=celebrity:
                        if not knows(person,celebrity) or knows(celebrity,person):
                            return False
            return True

        celebrity_candidate = 0
        for i in range(1,n):
            if not knows(i,celebrity_candidate):
                celebrity_candidate = i
        if is_celebrity(celebrity_candidate):
            return celebrity_candidate            
        return -1
    


                
                
                
        
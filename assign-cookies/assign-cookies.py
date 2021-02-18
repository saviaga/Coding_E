class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        k = 0
        c = 0
        counter = 0
        
        g.sort()
        s.sort()
        while k < len(g) and c <len(s):
            if s[c] >= g[k]:
                counter+=1
                k+=1
                c+=1
            else:
                c+=1
        return counter
        
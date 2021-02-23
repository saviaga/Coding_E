class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        count = 0
        cs = 0
        dict_elems = {}
        for i in range(len(A)):
            cs+=A[i]
            
            if  K!=0:
                cs = cs%K
                if cs == 0:
                    count+=1
            
            if cs in dict_elems:
                count+=dict_elems[cs]
                
            dict_elems[cs] =  dict_elems.get(cs,0)+1
        print(dict_elems)
        return count
        
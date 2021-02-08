class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust) < N - 1:
            return -1
        
        in_degrees = [0]* (N+1)
        out_degrees = [0]*(N+1)
        #save out and in degrees
        for relationship in trust:
            
            out_degrees[relationship[0]] += 1
            in_degrees[relationship[1]] += 1
        #there is no person 0
        for i in range(1,N+1):
            if in_degrees[i] == N-1 and out_degrees[i]==0:
                return i
        return -1
        
                
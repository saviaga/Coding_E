class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        carry = 0
        res = []
        p1 = len(num1)-1
        p2 = len(num2)-1
        while p1 >= 0 or p2 >= 0:
            n1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            n2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (n1+n2+carry)%10
            carry = (n1+n2+carry)//10
            res.append(value)
            p1-=1
            p2-=1
        if carry:
            res.append(carry)
            
        return "".join(str(x) for x in res[::-1])
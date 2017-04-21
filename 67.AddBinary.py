class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a)
        b = int(b)
        res = []
        car = 0 # carry
        
        if a ==0 and b==0:
            return "0"
        
        while a!=0 or b!=0:
            res.append(str(((a%10 + b%10)+car)%2))
            car = (a%10 + b%10+car)/2
            a = a/10
            b = b/10
        if car == 1:
            res.append("1")
        res.reverse()
        res = "".join(res)
        return res

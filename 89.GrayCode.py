class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0,1]
        if n == 1:
            return res
        elif n == 0:
            return [0]
        order = 1
        while order<n:
            count = len(res)
            while count!=0:
                res.append(res[count-1]+2**order)
                count = count -1 
            order = order + 1
        return res

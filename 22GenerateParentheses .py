class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        n = n*2
        self.n = n
        self.str_list = []
        self.res = []
        self.isBalanced(0,0,n,0)
        return self.res
        
    def isBalanced(self,left,right,n,direct):
        """
        direct = 0  left++  (
        direct = 1  right++ )
        """
        if direct == 0:
            left = left + 1
            self.str_list.append('(')
        else:
            right = right + 1
            self.str_list.append(')')
        n = n-1
        "stop"
        if (left == right) and (n == 0):
            self.res.append("".join(self.str_list))
            #self.str_list = []
            return
        "continue"
        if left >= right and n != 0:
            self.isBalanced(left,right,n,0)
            self.str_list = self.str_list[0:(self.n - n)]
            self.isBalanced(left,right,n,1)
            return
        "wrong"
        if left < right:
            return

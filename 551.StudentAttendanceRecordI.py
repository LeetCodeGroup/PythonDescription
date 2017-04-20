class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        1:A
        2:L
        3:P
        Less than 3 continuous L nor 2 A
        """
        L = 0
        A = 0
        pre = 'P'
        length = len(s)
        for item in range(length):
            if s[item] == 'A':
                A = A + 1
                L = 0
            elif s[item] == 'L' and (pre == 'L' or L==0):
                L = L+ 1
                pre = 'L'
            else:
                pre = 'P'
                L = 0
    
            if L >= 3:
                return False
            if A >= 2:
                return False
        return True
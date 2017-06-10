class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_h = len(haystack)
        len_n = len(needle)
        
        if len_h < len_n:
            return -1
        elif (len_h == 0) and (len_n == 0):
            return 0
        
        for sta in range(len_h-len_n+1):
            end = sta
            while (end-sta) < len_n:
                if haystack[end] == needle[end-sta]:
                    end = end + 1
                else:
                    break
            if end-sta == len_n:
                return sta
        
        return -1

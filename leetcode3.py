class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        p1 = 0
        p2 = 0
        val = 0
        num = 0
        memory = dict()
        if length == 0:
            return 0
        while p2<length:
            if (s[p2] in memory) and (memory[s[p2]]>=p1):
                p1 = memory[s[p2]] + 1
                memory[s[p2]] = p2
                p2 = p2+1
                num = p2 - p1
            elif (s[p2] not in memory) or (memory[s[p2]]<p1):
                memory[s[p2]]=p2
                p2=p2+1
                num = num + 1
            if num > val:
                val = num
                
        return val
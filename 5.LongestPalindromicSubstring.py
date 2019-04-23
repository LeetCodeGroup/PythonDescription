#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 15:43:34 2019

@author: huijian
"""

class Solution(object):
    # manacher algorithm
    def longestPalindrome(self,s):
        """
        :type s:str
        :rtype: str
        """
        new_str = ""
        for i in range(len(s)):
            new_str = new_str + "#" + s[i]
        
        new_str  = new_str + "#"
        
        # len(new_str) = 2*len(str) + 1
        
        p = [0 for i in range(len(new_str))]
        mx = 0
        idx = 0
        radius=0
        center=0
        #print(p)
        
        for i in range(len(new_str)):
            #print('*'*10)
            #print(i)
            if mx>i:
                #print(mx-i)
                p[i] = min(mx-i,p[2*idx-i])
            else:
                p[i] = 1
            #print(p[i])
            while (i>=p[i]) and ((i+p[i])<len(new_str)) and (new_str[i+p[i]]==new_str[i-p[i]]):
             #   print(p[i])
                p[i] = p[i]+1
             #   if (i<p[i]) or ((i+p[i])>=len(new_str)):
             #       break
            if p[i]+i>mx:
                idx = i
                mx= p[i]+i
            if p[i]>radius:
                radius=p[i]
                center = i
        
        shift = (center+1-radius)//2
        len_str = radius-1
        
        r_str = s[shift:shift+len_str]
        return r_str

if __name__=="__main__":
    sample_input="babad"
    solution = Solution()
    r_str = solution.longestPalindrome(s=sample_input)
    print(r_str)
                
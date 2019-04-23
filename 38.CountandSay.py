#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:36:12 2019

@author: huijian
"""

class Solution(object):
    def countAndSay(self,n):
        """
        type n int
        rtype: str
        """
        if n ==1:
            return "1"
        idx = 1
        in_str = "1"
        while idx < n:
            r_str = self.generate_new_s(in_str=in_str)
            in_str = r_str
            idx = idx+1
        return r_str
    def generate_new_s(self,in_str):
        last_char = None
        r_str=""
        count = 0
        for i in range(len(in_str)):
            char = in_str[i]
            if last_char is None:
                last_char = char
                count = 1
            elif last_char != char:
                r_str = r_str + str(count) + last_char
                last_char = char
                count = 1
            elif last_char == char:
                count = count+1
        if count!=0:
            r_str = r_str + str(count) + last_char
        return r_str

if __name__=="__main__":
    solution = Solution()
    r_str = solution.countAndSay(7)
    print(r_str)
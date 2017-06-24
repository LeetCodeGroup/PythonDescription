#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 20:15:57 2017

@author: huijian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depth, flag = self.check(root)
        return flag
    def check(self, node):
        if node == None:
            return (0,True)
        
        l_depth,l_flag = self.check(node.left)
        if l_flag == False:
            return -1,False
        r_depth,r_flag = self.check(node.right)
        if r_flag == False:
            return -1,False
        
        if abs(l_depth - r_depth) > 1:
            return -1, False
        else:
            depth = 1+max(l_depth,r_depth)
            return depth, True
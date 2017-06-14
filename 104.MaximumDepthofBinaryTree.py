#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:09:34 2017

@author: huijian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.todeep(root,self.depth)
        return self.depth
    
    def todeep(self,root,depth):
        if root == None:
            return
        depth = depth + 1
        if depth > self.depth:
            self.depth = depth
        self.todeep(root.left,depth)
        self.todeep(root.right,depth)
        
        return
        
        
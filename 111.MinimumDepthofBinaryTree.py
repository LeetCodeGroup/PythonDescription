#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 18:49:01 2017

@author: huijian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.depth = 0
        self.temp = []
        if root == None:
            return 0
        self.depth = 1
        self.temp.append(root)
        self.adddepth()
        return self.depth
    def adddepth(self):
        temp = []
        stop = False
        for item in self.temp:
            if item.right == None and item.left == None:
                stop = True
            if item.left!=None:
                temp.append(item.left)
            if item.right!=None:
                temp.append(item.right)
        if stop == True:
            return

        self.depth += 1
        self.temp = temp
        self.adddepth()
        return 
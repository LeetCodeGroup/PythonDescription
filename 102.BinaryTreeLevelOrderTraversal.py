#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:18:07 2017

@author: huijian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.nodes = []
        
        if root == None:
            return self.nodes
        else:
            self.addnode(0,root)
        
        return self.nodes
            
    def addnode(self,layer,root):
        if root == None:
            return
        if len(self.nodes) < (layer+1):
            self.nodes.append([])
        
        self.nodes[layer].append(root.val)
        self.addnode(layer+1,root.left)
        self.addnode(layer+1,root.right)
        
        return
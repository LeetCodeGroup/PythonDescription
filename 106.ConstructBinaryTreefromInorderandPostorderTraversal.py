#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 09:50:12 2017

@author: huijian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        Tree = self.subTree(inorder,postorder)
        return Tree
    def subTree(self, inord, postord):
        if len(postord) == 0:
            return None
        val = postord.pop(-1)
        node = TreeNode(val)
        
        if len(postord) == 0:
            node.right = None
            node.left = None
            return node
        
        index = 0
        for i in range(len(inord)):
            if inord[i] == val:
                index = i
                break
        
        left_inord = inord[0:index]
        right_inord = inord[index+1:]
        
        index = len(left_inord)-1
        left_post = postord[0:index+1]
        right_post = postord[index+1:len(postord)]
        
        node.left=self.subTree(left_inord, left_post)
        node.right = self.subTree(right_inord, right_post)
        
        return node
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 16:01:11 2017

@author: huijian
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        node = self.subtree(nums)
        return node
        
    def subtree(self,nums):
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            node = TreeNode(nums[0])
            return node
        
        mid = int((len(nums)+1)/2) - 1
        
        left_nums = nums[0:mid]
        right_nums = nums[mid+1:]
        
        node = TreeNode(nums[mid])
        node.left = self.subtree(left_nums)
        node.right = self.subtree(right_nums)
        
        return node
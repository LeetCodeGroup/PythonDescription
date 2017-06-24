#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 20:29:15 2017

@author: huijian
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        nums = []
        while head != None:
            nums.append(head.val)
            head = head.next
        Tree = self.subtree(nums)
        return Tree
        
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
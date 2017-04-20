# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        min_val = None
        max_val = None
        
        return self.checkRule(root,min_val,max_val)
        
    def checkRule(self,root,min_val,max_val):
        if root == None:
            return True
        if min_val != None and max_val != None:
            if min_val < root.val and max_val > root.val:
                return self.checkRule(root.left,min_val,root.val) and self.checkRule(root.right, root.val,max_val)
            else:
                return False
        if min_val == None and max_val != None:
            if root.val < max_val:
                return self.checkRule(root.left,min_val,root.val) and self.checkRule(root.right,root.val,max_val)
            else:
                return False
                
        if min_val != None and max_val == None:
            if root.val > min_val:
                return self.checkRule(root.left,min_val,root.val) and self.checkRule(root.right,root.val,max_val)
            else:
                return False
        if min_val == None and max_val == None:
            return self.checkRule(root.left,min_val,root.val) and self.checkRule(root.right,root.val,max_val)

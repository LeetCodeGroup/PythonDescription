# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.tree2sym(root.left,root.right)
    
    def tree2sym(self,left,right):
        if left == None and right == None:
            return True
        elif (left != None and right == None) or (left == None and right != None):
            return False
        elif (left != None and right != None) and (left.val == right.val):
            return self.tree2sym(left.left,right.right) and self.tree2sym(left.right, right.left)
        else:
            return False
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.tree = None
        self.tree = self.subTree(preorder, inorder)
        return self.tree
    
    def subTree(self,preorder, inorder):
        
        if len(preorder)==0:
            return None
        val = preorder.pop(0)
        node = TreeNode(val)
        
        if len(preorder)==0:
            node.right = None
            node.left = None
            return node
        
        index = 0
        for i in range(len(inorder)):
            if inorder[i] == val:
                index = i
                break

        left_inorder = inorder[0:index]
        right_inorder = inorder[index+1:]

        
        if len(left_inorder)==0:
            node.left = None
            node.right = self.subTree(preorder, right_inorder)
            return node
        
        index = len(left_inorder) - 1
        
        left_preorder = preorder[0:index+1]
        right_preorder = preorder[index+1:]

        
        node.left =self.subTree(left_preorder, left_inorder)
        node.right = self.subTree(right_preorder, right_inorder)
        
        return node
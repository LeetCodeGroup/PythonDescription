# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.nodes = []
        if root == None:
            return self.nodes
        self.temp = [root]
        toleft = 0
        while len(self.temp)!=0:
            self.travelthelist(toleft)
            toleft = 1 - toleft
        return self.nodes
        
    def travelthelist(self,toleft):
        temp = []
        tempnodes = []
        index = -1
        
        length = len(self.temp)
        while length != 0:
            item = self.temp.pop(index)
            length = length - 1
            tempnodes.append(item.val)
            if toleft == 1:
                if item.right != None:
                    temp.append(item.right)
                if item.left != None:
                    temp.append(item.left)
            elif toleft == 0:    
                if item.left != None:
                    temp.append(item.left)
                if item.right != None:
                    temp.append(item.right)
        
        self.temp = temp
        self.nodes.append(tempnodes)
        return
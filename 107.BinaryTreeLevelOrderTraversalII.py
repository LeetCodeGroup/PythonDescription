# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.nodes=[]
        self.temp = []
        if root == None:
            return self.nodes
        self.temp.append(root)
        self.bfs()
        self.nodes.reverse()
        return self.nodes
        
    
    def bfs(self):
        level_nodes = []
        temp = []
        if len(self.temp) == 0:
            return
        for item in self.temp:
            level_nodes.append(item.val)
            if item.left!=None:
                temp.append(item.left)
            if item.right!=None:
                temp.append(item.right)

        self.temp = temp
        self.nodes.append(level_nodes[:])
        self.bfs()
        return
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.tran = []
        self.inorder(root)
        
        print(self.tran)
        res = abs(self.tran[1] - self.tran[0])
        for i in range(len(self.tran) - 1):
            if abs(self.tran[i] - self.tran[i+1]) < res:
                res = abs(self.tran[i] - self.tran[i+1])
                
        return res
        
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.tran.append(root.val)
        self.inorder(root.right)
        
        

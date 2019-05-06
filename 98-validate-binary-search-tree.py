# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        tree = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            tree.append(root.val)
            inorder(root.right)
            
        inorder(root)
        
        for i in range(len(tree)-1):
            if tree[i] >= tree[i+1]:
                return False
        
        return True
            
        

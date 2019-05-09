# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if root is None:
            return res
        
        stack = []
        stack.append(root)
        
        while stack:
            root = stack.pop()
            res.append(root.val)
            
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
        
        
        return res
    

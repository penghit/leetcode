# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        

        if root is None:
            return True
    
    
        def height(root):
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        stack = []
        stack.append(root)
        
        while stack:
            root = stack.pop()
            if abs(height(root.left) - abs(height(root.right))) > 1:
                return False
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        
        
        return True

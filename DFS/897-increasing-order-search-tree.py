# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        res = []
        
        def inorder(root, res):
            if root is None:
                return
            inorder(root.left, res)
            res.append(root.val)
            res.append(None)
            inorder(root.right, res)

            
        inorder(root, res)
        res.pop()
        return res
        

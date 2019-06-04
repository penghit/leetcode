# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        # this function checks if left is a mirror of right
        def isMirror(left, right):
            # if left and right are both none, return true, else return false
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            
            return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        
        return isMirror(root, root)

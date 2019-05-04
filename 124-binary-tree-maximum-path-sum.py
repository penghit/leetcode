# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        
        
        def maxgain(root):
            nonlocal maxsum
            if root is None:
                return 0
            
            leftgain = max(maxgain(root.left), 0)
            rightgain = max(maxgain(root.right), 0)
            
            newpath = root.val + leftgain + rightgain
            
            maxsum = max(maxsum, newpath)
            
            return max(leftgain + root.val, rightgain + root.val)
        
        maxsum = float('-inf')
        maxgain(root)
        return maxsum

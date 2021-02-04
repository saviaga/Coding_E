# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def diameterHelper(root):
            if root is None:
                return 0
            
            L = diameterHelper(root.left)
            R = diameterHelper(root.right)
            self.ans = max(self.ans, L+R+1)
            return max(L,R)+1
        
        
        
        
        self.ans = 1
        diameterHelper(root)
        return self.ans -1
        
        
        
                
            
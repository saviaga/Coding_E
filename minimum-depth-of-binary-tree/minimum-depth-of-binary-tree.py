# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
       
        if root is None:
            return 0
        
        stack = [(root,1)]
        ans = []
        min_depth = float('inf')
        while stack:
            current,depth = stack.pop()
            
            if not current.left and not current.right:
                min_depth = min(min_depth, depth)
            if current.right:
                stack.append((current.right,depth+1))
            if current.left:
                stack.append((current.left,depth+1))
        
        return min_depth
        
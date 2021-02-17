# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return
        
        stack = [root]
        
        while stack:
            current = stack.pop()
            temp_left = current.left
           
            #swap children
            current.left = current.right
            current.right = temp_left
            
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
            
        return root
        

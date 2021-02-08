# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root is None:
            return
        res = []
        stack = [root]
        suma = 0
        while stack:
            current = stack.pop()
            if current.val >= low and current.val <=high:
                suma+=current.val
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return suma
                
        
        
        